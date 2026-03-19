#!/bin/bash
# Generate blueprint web documentation

# Add leanblueprint to PATH
export PATH="/Users/pmahon/Library/Python/3.10/bin:$PATH"

echo "📚 Generating blueprint web documentation..."

# Generate the web version
cd "$(dirname "$0")"
leanblueprint web

echo "✅ Blueprint generated!"
echo ""
echo "Open: blueprint/web/index.html"
