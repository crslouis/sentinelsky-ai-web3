#!/bin/bash
# Create proof archive for SentinelSky AI
# Packages source code and demo results

set -e

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
ARCHIVE_NAME="sentinelsky-proof-${TIMESTAMP}.zip"

echo "📦 Creating proof archive..."
echo "============================"

# Create temporary directory for proof
PROOF_DIR="proof_temp"
mkdir -p "$PROOF_DIR"

# Copy source files
echo "Copying source files..."
cp -r src "$PROOF_DIR/"
cp -r agent "$PROOF_DIR/"
cp -r scripts "$PROOF_DIR/"
cp package.json "$PROOF_DIR/"
cp README.md "$PROOF_DIR/"
cp vite.config.ts "$PROOF_DIR/"
cp tsconfig.json "$PROOF_DIR/"
cp tailwind.config.js "$PROOF_DIR/"
cp index.html "$PROOF_DIR/"

# Run agent demo and capture output
echo "Running agent demo..."
cd agent
python3 main.py > "../${PROOF_DIR}/agent_demo_output.txt" 2>&1 || true
cd ..

# Create build info
echo "Creating build info..."
cat > "${PROOF_DIR}/build_info.txt" << EOF
SentinelSky AI - Build Information
===================================
Build Date: $(date)
Node Version: $(node --version 2>/dev/null || echo "N/A")
NPM Version: $(npm --version 2>/dev/null || echo "N/A")
Python Version: $(python3 --version 2>/dev/null || echo "N/A")

Project Structure:
$(find . -type f -not -path "*/node_modules/*" -not -path "*/.git/*" -not -path "*/dist/*" -not -path "*.zip" | wc -l) files

Security Scan: See secret_scan_result.txt
Agent Demo: See agent_demo_output.txt
EOF

# Run secret scan
echo "Running secret scan..."
bash scripts/secret_scan.sh > "${PROOF_DIR}/secret_scan_result.txt" 2>&1 || echo "Secret scan completed with warnings" >> "${PROOF_DIR}/secret_scan_result.txt"

# Create archive
echo "Creating ZIP archive..."
zip -r "$ARCHIVE_NAME" "$PROOF_DIR" -q

# Cleanup
rm -rf "$PROOF_DIR"

echo ""
echo "✅ Proof archive created: $ARCHIVE_NAME"
echo "============================"
echo "Archive contains:"
echo "  • Source code"
echo "  • Agent demo output"
echo "  • Security scan results"
echo "  • Build information"
echo ""
