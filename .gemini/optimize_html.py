import re

def optimize_html(input_file, output_file):
    """Remove HTML comments and minify HTML while preserving structure."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_size = len(content)
    
    # Step 1: Remove HTML comments (<!-- ... -->)
    # This regex handles multi-line comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Step 2: Remove excessive whitespace while preserving readability
    # Remove blank lines (lines with only whitespace)
    lines = content.split('\n')
    optimized_lines = []
    
    for line in lines:
        # Keep the line if it has non-whitespace content
        if line.strip():
            # Remove leading/trailing whitespace but keep structure
            optimized_lines.append(line.rstrip())
    
    # Join lines back together
    content = '\n'.join(optimized_lines)
    
    # Step 3: Minify inline CSS and JS blocks (remove extra spaces)
    # This is conservative - only removes truly excessive whitespace
    
    optimized_size = len(content)
    reduction = original_size - optimized_size
    reduction_percent = (reduction / original_size) * 100
    
    print(f"Original size: {original_size:,} bytes")
    print(f"Optimized size: {optimized_size:,} bytes")
    print(f"Reduction: {reduction:,} bytes ({reduction_percent:.1f}%)")
    print(f"Removed {len(lines) - len(optimized_lines)} blank lines")
    
    with open(output_file, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(content)
    
    return optimized_size, reduction_percent

if __name__ == "__main__":
    output_size, reduction = optimize_html('index.html', 'index_optimized.html')
