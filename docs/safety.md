# Safety Guidelines

## Core Principles

SentinelSky AI is designed with **human-in-the-loop safety** as a fundamental principle. We provide intelligence and analysis, but **never** take autonomous actions that could compromise user security or funds.

## What We DO NOT Do

### ❌ No Private Key Handling
- **Never** request private keys from users
- **Never** store private keys
- **Never** transmit private keys to any API
- **Never** use private keys for any purpose

**Why**: Private keys are the sole ownership proof of crypto assets. Exposing them means complete loss of funds.

### ❌ No Seed Phrase Handling
- **Never** request seed phrases (recovery phrases)
- **Never** store seed phrases
- **Never** transmit seed phrases to any API
- **Never** use seed phrases for wallet recovery

**Why**: Seed phrases provide full access to all accounts derived from them. Compromising a seed phrase means losing all associated assets.

### ❌ No Auto-Signing
- **Never** automatically sign transactions
- **Never** sign transactions without explicit user approval
- **Never** use wallet signing APIs without user interaction
- **Never** bypass wallet confirmation dialogs

**Why**: Transaction signing is the final authorization step. Auto-signing could result in unauthorized fund transfers.

### ❌ No Auto-Claiming
- **Never** automatically claim airdrops or rewards
- **Never** execute on-chain transactions without approval
- **Never** interact with smart contracts on behalf of users
- **Never** submit transactions to blockchain networks

**Why**: Even "safe" transactions can have unintended consequences. Users must review and approve every on-chain action.

### ❌ No CAPTCHA Bypass
- **Never** use AI to solve CAPTCHAs
- **Never** use CAPTCHA-solving services
- **Never** automate CAPTCHA submission
- **Never** bypass bot detection mechanisms

**Why**: CAPTCHAs exist to prevent automated abuse. Bypassing them enables Sybil attacks and violates platform terms of service.

### ❌ No Sybil Farming
- **Never** create multiple fake accounts
- **Never** automate account creation
- **Never** use multiple wallets to game airdrops
- **Never** engage in wash trading or fake activity

**Why**: Sybil attacks harm legitimate users and projects. They violate platform rules and can result in bans or legal consequences.

### ❌ No Spam Automation
- **Never** send unsolicited messages
- **Never** automate social media posting
- **Never** create fake engagement (likes, follows, retweets)
- **Never** participate in coordinated inauthentic behavior

**Why**: Spam and fake engagement pollute platforms and harm user experience. They violate terms of service and can result in account suspension.

## What We DO

### ✅ Read-Only Analysis
- **Analyze** public blockchain data
- **Monitor** public threat feeds
- **Scan** smart contract source code
- **Evaluate** tokenomics and distribution

**How**: All data comes from public sources (block explorers, GitHub, social media). No privileged access required.

### ✅ Intelligence Gathering
- **Detect** phishing domains
- **Identify** rugpull patterns
- **Discover** smart contract vulnerabilities
- **Track** scam campaigns

**How**: AI-powered pattern recognition on public data. No interaction with malicious sites or contracts.

### ✅ Risk Assessment
- **Score** project risk levels
- **Evaluate** team transparency
- **Assess** tokenomics health
- **Compare** against industry standards

**How**: Multi-factor analysis using Xiaomi MiMo AI. Human-readable reports with clear reasoning.

### ✅ Educational Content
- **Explain** security concepts
- **Teach** threat recognition
- **Provide** best practices
- **Share** threat intelligence

**How**: Clear, actionable guidance. No technical jargon. Multilingual support.

### ✅ Human Review Required
- **Present** findings to users
- **Recommend** actions (but never execute)
- **Require** explicit approval for any action
- **Defer** to user judgment

**How**: All reports include recommendations, but users must decide and act themselves.

## Public Demo Safety

### Mock Data Only
The public demo at [sentinelsky.ai](https://sentinelsky.ai) uses **100% mock data**:

- ✅ **Fake contract addresses**: Not real blockchain contracts
- ✅ **Fake threat data**: Simulated phishing sites and scams
- ✅ **Fake analysis results**: Pre-generated reports
- ✅ **No real API calls**: No actual MiMo API usage
- ✅ **No real blockchain data**: No connection to real networks

**Why**: Public demos must not expose real threats or vulnerabilities before responsible disclosure. Mock data demonstrates capabilities without risk.

### No Real Credentials
The public demo **never** uses real credentials:

- ❌ No real MiMo API keys
- ❌ No real blockchain RPC endpoints
- ❌ No real database connections
- ❌ No real user data

**Why**: Public demos are accessible to anyone. Real credentials would be exposed and abused.

### Clear Labeling
All mock data is clearly labeled:

```
⚠️ DEMO MODE: Using mock data only
This is a demonstration. No real threats are detected.
No real blockchain data is analyzed.
```

**Why**: Users must understand they're seeing a demo, not real threat intelligence.

## Admin-Only Real Workflow

### Production Access Control
Real threat detection is **admin-only**:

```python
@require_admin
async def scan_real_contract(address: str):
    # Only admins can trigger real scans
    return await contract_scanner.scan(address)
```

**Why**: Real threat detection requires:
- Responsible disclosure processes
- Legal compliance
- Ethical guidelines
- Human oversight

### Responsible Disclosure
When real vulnerabilities are found:

1. **Private notification** to project team
2. **Grace period** for fixes (typically 90 days)
3. **Public disclosure** only after fix or grace period
4. **No exploitation** of vulnerabilities

**Why**: Responsible disclosure protects users while giving projects time to fix issues.

### Legal Compliance
All operations comply with:

- **GDPR**: No personal data collection without consent
- **CCPA**: California privacy rights
- **DMCA**: Respect intellectual property
- **Terms of Service**: Follow platform rules

**Why**: Legal compliance protects both users and the project.

## User Safety Guidelines

### For Users
When using SentinelSky AI:

1. **Never share private keys or seed phrases** with anyone, including us
2. **Always verify** findings independently
3. **Use multiple sources** for critical decisions
4. **Understand** that AI can make mistakes
5. **Take responsibility** for your own security

### For Developers
When integrating SentinelSky AI:

1. **Never send** private keys or seed phrases to our API
2. **Always use** server-side API calls (never client-side)
3. **Implement** rate limiting and abuse prevention
4. **Cache** results to reduce API calls
5. **Handle errors** gracefully

### For Projects
When being analyzed by SentinelSky AI:

1. **Welcome** security research
2. **Provide** clear contact information
3. **Respond** to vulnerability reports promptly
4. **Fix** issues before public disclosure
5. **Thank** researchers for responsible disclosure

## Incident Response

### If We Detect a Critical Threat

1. **Verify** the threat is real (not false positive)
2. **Assess** the severity and impact
3. **Notify** affected parties privately
4. **Coordinate** with security community
5. **Disclose** publicly after mitigation

### If We Make a Mistake

1. **Acknowledge** the error immediately
2. **Correct** the information
3. **Notify** affected parties
4. **Analyze** root cause
5. **Improve** processes to prevent recurrence

### If Our System is Compromised

1. **Shut down** affected services immediately
2. **Investigate** the breach
3. **Notify** users transparently
4. **Remediate** vulnerabilities
5. **Restore** services only after verification

## Ethical AI Use

### Transparency
- **Disclose** when AI is used
- **Explain** AI limitations
- **Provide** reasoning for decisions
- **Allow** human override

### Fairness
- **No discrimination** based on user attributes
- **Equal access** to threat intelligence
- **No preferential treatment** for paying customers
- **Community-first** approach

### Accountability
- **Human oversight** for critical decisions
- **Audit trails** for all actions
- **Clear responsibility** for outcomes
- **Continuous improvement** based on feedback

### Privacy
- **Minimize** data collection
- **Anonymize** user data
- **Encrypt** sensitive information
- **Delete** data when no longer needed

## Red Lines (Never Cross)

1. **Never** handle private keys or seed phrases
2. **Never** execute transactions without explicit approval
3. **Never** bypass security measures (CAPTCHAs, 2FA)
4. **Never** engage in Sybil attacks or fake activity
5. **Never** exploit vulnerabilities for personal gain
6. **Never** sell user data to third parties
7. **Never** use AI to manipulate or deceive users
8. **Never** prioritize profit over user safety

## Conclusion

SentinelSky AI is a **security intelligence platform**, not an automation tool. We provide:

- ✅ **Intelligence**: Threat detection and analysis
- ✅ **Recommendations**: Actionable security advice
- ✅ **Education**: Security awareness and best practices

We **never** provide:

- ❌ **Automation**: No auto-signing, auto-claiming, or auto-trading
- ❌ **Exploitation**: No vulnerability exploitation or abuse
- ❌ **Deception**: No fake activity or Sybil attacks

**Our mission**: Protect Web3 users through AI-powered intelligence, while respecting human agency and ethical boundaries.

---

**For more information**:
- [Application Description](./application_description.md)
- [Architecture](./architecture.md)
- [MiMo Integration](./mimo_integration.md)
- [Token Consumption](./token_consumption.md)
