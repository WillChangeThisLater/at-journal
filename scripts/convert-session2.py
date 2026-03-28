#!/usr/bin/env python3
import json
import sys

def format_content(content):
    """Format content array to HTML string"""
    html_parts = []
    for item in content:
        item_type = item.get('type')
        if item_type == 'text':
            text = item.get('text', '')
            if '```' in text:
                parts = text.split('```')
                for i, part in enumerate(parts):
                    if i % 2 == 1:
                        code = part.strip()
                        if 'bash' in code or '$ ' in code:
                            html_parts.append(f'<div class="code-block">{code.replace("```", "")}</div>')
                        else:
                            html_parts.append(f'<code>{code.replace("```", "")}</code>')
                    else:
                        safe_text = text.replace('<', '&lt;').replace('>', '&gt;')
                        html_parts.append(f'<p>{safe_text}</p>')
            else:
                safe_text = text.replace('<', '&lt;').replace('>', '&gt;')
                html_parts.append(f'<p>{safe_text}</p>')
        elif item_type == 'toolCall':
            call = item.get('toolCall', {})
            name = call.get('name', 'unknown')
            args = call.get('arguments', '{}')
            html_parts.append(f'<div class="tool-call"><strong>{name}</strong>')
            if isinstance(args, dict):
                for k, v in args.items():
                    html_parts.append(f'<span style="color:#6b7280">{k}:</span> <code>{v}</code>')
            elif isinstance(args, str):
                html_parts.append(f'<code>{args}</code>')
            html_parts.append('</div>')
        elif item_type == 'thinking':
            thinking = item.get('thinking', '')
            html_parts.append(f'<div class="thinking-box"><strong>Thinking:</strong> {thinking}</div>')
        elif item_type == 'toolResult':
            result = item.get('toolResult', {})
            tool_name = result.get('toolName', 'result')
            content = result.get('content', [])
            is_error = result.get('isError', False)
            error_class = 'log-error' if is_error else ''
            html_parts.append(f'<div class="tool-result {error_class}">')
            html_parts.append(f'<strong style="color:#2563eb">{tool_name}</strong>')
            for item in content:
                if item.get('type') == 'text':
                    text = item.get('text', '')
                    if '```' in text:
                        parts = text.split('```')
                        for i, part in enumerate(parts):
                            if i % 2 == 1:
                                html_parts.append(f'<div class="code-block">{part.strip().replace("```", "")}</div>')
                            else:
                                safe = text.replace('<', '&lt;').replace('>', '&gt;')
                                html_parts.append(f'<p>{safe}</p>')
                    else:
                        safe = text.replace('<', '&lt;').replace('>', '&gt;')
                        html_parts.append(f'<p>{safe}</p>')
            html_parts.append('</div>')
    return '\n'.join(html_parts)

def convert(jsonl_path, output_path):
    with open(jsonl_path, 'r') as f:
        lines = f.readlines()
    
    session_meta = json.loads(lines[0])
    messages = []
    
    for line in lines[1:]:
        msg = json.loads(line)
        content = msg.get('message', {}).get('content', [])
        formatted = format_content(content)
        
        messages.append({
            'role': 'user' if msg.get('role') == 'user' else 'assistant',
            'timestamp': msg.get('timestamp', ''),
            'content': formatted
        })
    
    # Write as JSON for JavaScript to consume
    with open(output_path, 'w') as f:
        json.dump(messages, f, indent=2)
    
    print(f"Converted {len(messages)} messages")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 convert-session2.py <input.jsonl> <output.json>")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
