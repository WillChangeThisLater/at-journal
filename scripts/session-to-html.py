#!/usr/bin/env python3
"""
Convert pi-agent session JSONL to HTML for blog post display
"""

import json
import sys
from datetime import datetime

def format_timestamp(ts):
    """Format ISO timestamp to readable format"""
    return datetime.fromisoformat(ts).strftime("%Y-%m-%d %H:%M:%S")

def format_tool_call(call):
    """Format a tool call to HTML"""
    name = call.get('name', 'unknown')
    args = call.get('arguments', '{}')
    
    html = f'<div class="tool-call"><strong>{name}</strong>'
    
    if isinstance(args, dict):
        for key, value in args.items():
            if key == 'path' or key == 'command':
                html += f'<code>{value}</code>'
            else:
                html += f'<span class="tool-key">{key}</span>: <span class="tool-value">{value}</span>'
    elif isinstance(args, str):
        html += f'<code>{args}</code>'
    
    html += '</div>'
    return html

def format_message(msg):
    """Format a message to HTML"""
    role = msg.get('role', 'unknown')
    content = msg.get('message', {}).get('content', [])
    timestamp = format_timestamp(msg.get('timestamp', ''))
    
    html = f'<div class="message {role}" data-timestamp="{timestamp}">'
    
    # Process content array
    for item in content:
        if item.get('type') == 'text':
            text = item.get('text', '')
            # Handle code blocks
            if '```bash' in text or '```' in text:
                parts = text.split('```')
                for i, part in enumerate(parts):
                    if i % 2 == 1:  # Code block
                        html += f'<pre><code>{part.strip()}</code></pre>\n'
                    else:
                        # Regular text - escape HTML
                        safe_text = text.replace('<', '&lt;').replace('>', '&gt;')
                        html += f'<p>{safe_text}</p>\n'
            else:
                # Regular text
                safe_text = text.replace('<', '&lt;').replace('>', '&gt;')
                html += f'<p>{safe_text}</p>\n'
        
        elif item.get('type') == 'toolCall':
            call = item.get('toolCall', {})
            call_id = call.get('id', '')
            name = call.get('name', 'unknown')
            args = call.get('arguments', '{}')
            api = call.get('api', '')
            provider = call.get('provider', '')
            model = call.get('model', '')
            
            html += f'<div class="tool-use">\n'
            html += f'<span class="tool-call-id">[{call_id[:8]}]</span> '
            html += f'<span class="tool-name">{name}</span>'
            
            if args:
                html += format_tool_call(call)
            
            html += f'</div>'
        
        elif item.get('type') == 'thinking':
            thinking = item.get('thinking', '')
            html += f'<div class="thinking">\n'
            html += f'<span class="thinking-label">Thinking:</span> {thinking}\n'
            html += '</div>'
        
        elif item.get('type') == 'toolResult':
            tool_result = item.get('toolResult', {})
            tool_name = tool_result.get('toolName', 'unknown')
            tool_call_id = tool_result.get('toolCallId', '')
            content = tool_result.get('content', [])
            is_error = tool_result.get('isError', False)
            
            error_class = 'error' if is_error else ''
            html += f'<div class="tool-result {error_class}">\n'
            html += f'<span class="tool-result-name">{tool_name}</span> '
            html += f'<span class="tool-result-id">[{tool_call_id[:8]}]</span>'
            
            for item in content:
                if item.get('type') == 'text':
                    text = item.get('text', '')
                    # Handle code blocks
                    if '```bash' in text or '```' in text:
                        parts = text.split('```')
                        for i, part in enumerate(parts):
                            if i % 2 == 1:  # Code block
                                html += f'<pre><code>{part.strip()}</code></pre>\n'
                            else:
                                safe_text = text.replace('<', '&lt;').replace('>', '&gt;')
                                html += f'<p>{safe_text}</p>\n'
                    else:
                        safe_text = text.replace('<', '&lt;').replace('>', '&gt;')
                        html += f'<p>{safe_text}</p>\n'
            
            html += '</div>'
    
    html += '</div>'
    return html

def convert_session(jsonl_path, output_path):
    """Convert JSONL session to HTML"""
    
    with open(jsonl_path, 'r') as f:
        lines = f.readlines()
    
    # First line is session metadata
    session_meta = json.loads(lines[0])
    
    html_parts = [
        '<div class="session-metadata">',
        f'<h3>Session Details</h3>',
        f'<p><strong>ID:</strong> {session_meta.get("id", "unknown")}</p>',
        f'<p><strong>Timestamp:</strong> {session_meta.get("timestamp", "unknown")}</p>',
        f'<p><strong>Working Directory:</strong> {session_meta.get("cwd", "unknown")}</p>',
        f'<p><strong>Model:</strong> {session_meta.get("model", "unknown")}</p>',
        f'<p><strong>Thinking:</strong> {session_meta.get("thinkingLevel", "unknown")}</p>',
        '</div>\n',
        '<div class="session-messages">',
    ]
    
    for line in lines[1:]:
        msg = json.loads(line)
        html_parts.append(format_message(msg))
    
    html_parts.append('</div>')
    
    with open(output_path, 'w') as f:
        f.write('\n'.join(html_parts))
    
    print(f"Converted {len(lines) - 1} messages to {output_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 session-to-html.py <input.jsonl> <output.html>")
        sys.exit(1)
    
    convert_session(sys.argv[1], sys.argv[2])
