#!/bin/bash
# Secret Scan Script for SentinelSky AI
# Ensures no sensitive data is committed

set -e

echo "🔒 Running Secret Scan..."
echo "=========================="

# Patterns to search for
PATTERNS=(
    "private.?key"
    "seed.?phrase"
    "mnemonic"
    "api.?key"
    "secret.?key"
    "password"
    "0x[a-fA-F0-9]{64}"  # Private keys
    "sk_live_"           # Stripe live keys
    "sk_test_"           # Stripe test keys
)

FOUND=0

for pattern in "${PATTERNS[@]}"; do
    echo "Checking for: $pattern"
    if grep -rniE "$pattern" . \
        --exclude-dir=node_modules \
        --exclude-dir=.git \
        --exclude-dir=dist \
        --exclude="*.zip" \
        --exclude="secret_scan.sh" 2>/dev/null; then
        echo "⚠️  WARNING: Potential secret found matching: $pattern"
        FOUND=1
    fi
done

if [ $FOUND -eq 0 ]; then
    echo ""
    echo "✅ No secrets detected"
    echo "=========================="
    exit 0
else
    echo ""
    echo "❌ Potential secrets found!"
    echo "Please review and remove before committing."
    echo "=========================="
    exit 1
fi
