# SentinelSky AI

**Web3 Intelligence Platform with Human-in-the-Loop Safety**

SentinelSky AI is an intelligent monitoring and automation platform for Web3 opportunities, powered by **Xiaomi MiMo AI models**. It helps users track airdrops, testnets, and DeFi protocols while maintaining complete control and transparency.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Powered by Xiaomi MiMo](https://img.shields.io/badge/Powered%20by-Xiaomi%20MiMo-blue)](https://www.mi.com/global/discover/article?id=3188)

---

## 🛡️ Safety First

- ✅ Human approval required for all transactions
- ✅ No private keys or seed phrases stored
- ✅ Transparent operation logs and audit trails
- ✅ Read-only analysis, no autonomous actions
- ✅ Public demo uses mock data only

**[Read Full Safety Guidelines →](./docs/safety.md)**

---

## 🚀 Features

### Intelligent Monitoring
Track airdrops, testnets, and DeFi opportunities across multiple chains in real-time using AI-powered threat detection.

### Smart Analysis
- **Phishing Detection**: Identify fake websites and scam campaigns
- **Rugpull Risk Scoring**: Analyze liquidity, team, and contract risks
- **Smart Contract Scanning**: Detect vulnerabilities before they're exploited
- **Tokenomics Analysis**: Evaluate token distribution and vesting schedules

### Multilingual Intelligence
Global threat coverage across 50+ languages, powered by Xiaomi MiMo's multilingual capabilities.

### Human-in-the-Loop Safety
Every action requires explicit user approval. No auto-signing, no auto-claiming, no autonomous transactions.

---

## 🤖 AI-Powered by Xiaomi MiMo

SentinelSky AI uses **Xiaomi MiMo V2.5** and **MiMo V2.5 Pro** for all intelligence tasks:

- **MiMo V2.5**: Extraction, summarization, multilingual research
- **MiMo V2.5 Pro**: Deep reasoning, risk scoring, vulnerability analysis

### Token Consumption

| Agent | Tokens/Run | Runs/Day | Daily Tokens |
|---|---:|---:|---:|
| Threat Scout | 120K | 24 | 2.88M |
| Phishing Detector | 180K | 30 | 5.4M |
| Contract Scanner | 450K | 20 | 9M |
| Rugpull Risk | 350K | 20 | 7M |
| Tokenomics Analyst | 300K | 15 | 4.5M |
| Social Trust | 150K | 20 | 3M |
| Report Generator | 250K | 10 | 2.5M |
| Multilingual Research | 250K | 15 | 3.75M |
| **TOTAL** | | | **38M/day** |

**Monthly**: ~1.14B tokens  
**Community Scale**: 5B+ tokens/month

**[Read Full Token Consumption Model →](./docs/token_consumption.md)**

---

## 📦 Project Structure

```
sentinelsky-ai/
├── src/              # React frontend (landing page)
├── agent/            # Python agent demo (mock data)
├── docs/             # Documentation (7 files)
├── reports/          # Sample threat reports (5 files)
├── data/             # Token usage and sample data
├── scripts/          # Security and validation scripts
└── public/           # Static assets
```

---

## 🔧 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.8+
- npm or yarn

### Installation

```bash
# Clone repository
git clone https://github.com/username/sentinelsky-ai.git
cd sentinelsky-ai

# Install dependencies
npm install

# Run development server
npm run dev
```

### Build for Production

```bash
# Build frontend
npm run build

# Output in dist/
```

### Run Agent Demo

```bash
# Run Python agent with mock data
cd agent
python3 main.py
```

**Note**: The agent demo uses 100% mock data. No real MiMo API calls, no real blockchain data.

---

## 📚 Documentation

### Core Documentation
- **[Application Description](./docs/application_description.md)** - Overview, problem statement, solution
- **[Architecture](./docs/architecture.md)** - System design, multi-agent architecture
- **[Token Consumption](./docs/token_consumption.md)** - Detailed token usage model
- **[MiMo Integration](./docs/mimo_integration.md)** - How we use Xiaomi MiMo
- **[Safety Guidelines](./docs/safety.md)** - Security principles and red lines
- **[Roadmap](./docs/roadmap.md)** - Development timeline and milestones
- **[Proof Materials](./docs/proof_materials.md)** - Xiaomi MiMo Orbit 100T submission

### Sample Reports
- **[Daily Threat Digest](./reports/sample_daily_threat_digest.md)** - 24-hour threat summary
- **[Phishing Report](./reports/sample_phishing_report.md)** - Fake Uniswap airdrop analysis
- **[Contract Risk Report](./reports/sample_contract_risk_report.md)** - Reentrancy vulnerability analysis
- **[Rugpull Report](./reports/sample_rugpull_report.md)** - MoonDoge Finance risk assessment
- **[Tokenomics Report](./reports/sample_tokenomics_report.md)** - DFAP token analysis

---

## 🎯 Use Cases

### For Individual Users
- Verify airdrop legitimacy before claiming
- Check smart contract security before depositing
- Assess rugpull risk before investing
- Monitor daily threats in Web3 ecosystem

### For DeFi Traders
- Analyze token economics before buying
- Detect phishing sites targeting traders
- Evaluate protocol security
- Track emerging threats

### For Security Researchers
- Access threat intelligence data
- Contribute to community security
- Research attack patterns
- Collaborate on threat detection

---

## 🔒 Security

### What We DO NOT Do
- ❌ No private keys or seed phrases
- ❌ No auto-signing or auto-claiming
- ❌ No CAPTCHA bypass
- ❌ No Sybil farming
- ❌ No spam automation

### What We DO
- ✅ Read-only blockchain analysis
- ✅ Public data intelligence gathering
- ✅ Risk assessment and scoring
- ✅ Educational content and best practices
- ✅ Human review required for all actions

**[Read Full Safety Guidelines →](./docs/safety.md)**

---

## 🌐 Live Demo

**URL**: https://sentinelsky.vercel.app (after deployment)

**Important**: The public demo uses **100% mock data** for safety and responsible disclosure:
- ✅ Fake contract addresses
- ✅ Fake threat data
- ✅ Pre-generated reports
- ✅ No real MiMo API calls
- ✅ No real blockchain data

---

## 🛠️ Technology Stack

### Frontend
- React 18 + TypeScript
- Tailwind CSS
- Vite
- Lucide React (icons)

### Backend (Future)
- Python FastAPI
- PostgreSQL
- Redis
- Celery

### AI Models
- Xiaomi MiMo V2.5 (extraction, summarization)
- Xiaomi MiMo V2.5 Pro (reasoning, risk scoring)

### Infrastructure
- Vercel (frontend hosting)
- AWS/GCP (backend, future)
- Cloudflare (CDN, DDoS protection)

---

## 📈 Roadmap

### Phase 1: MVP (Q2 2026) ✅ Current
- Landing page and public demo
- 8 specialized AI agents (mock data)
- Documentation and proof materials
- Xiaomi MiMo integration design

### Phase 2: Beta (Q3 2026)
- Live threat detection with real data
- User authentication and accounts
- API endpoints for developers
- Email/Telegram alerts

### Phase 3: Production (Q4 2026)
- Mobile app (iOS + Android)
- Browser extension (Chrome + Firefox)
- Advanced analytics dashboard
- Enterprise tier

### Phase 4: Scale (2027)
- Global expansion
- White-label offering
- Advanced AI features
- Decentralized threat database

**[Read Full Roadmap →](./docs/roadmap.md)**

---

## 🤝 Contributing

We welcome contributions! Please read our contributing guidelines before submitting PRs.

### Areas for Contribution
- Additional threat detection agents
- Improved phishing detection algorithms
- New blockchain network support
- Documentation improvements
- Bug reports and feature requests

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Xiaomi MiMo Team** - For providing powerful AI models
- **Web3 Security Community** - For threat intelligence and research
- **Open Source Contributors** - For tools and libraries

---

## 📞 Contact

- **GitHub**: https://github.com/username/sentinelsky-ai
- **Twitter**: @SentinelSkyAI (future)
- **Telegram**: t.me/sentinelskyai (future)
- **Discord**: discord.gg/sentinelskyai (future)

---

## ⚠️ Disclaimer

This is a demonstration platform for Xiaomi MiMo Orbit 100T submission. The public demo uses mock data only. Always verify transactions independently and never share private keys or seed phrases with any automated system.

**Not financial advice. Always DYOR (Do Your Own Research).**

---

**Built with ❤️ for the Web3 community**  
**Powered by Xiaomi MiMo AI**
