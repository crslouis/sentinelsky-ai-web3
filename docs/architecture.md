# SentinelSky AI - System Architecture

## Overview

SentinelSky AI uses a **multi-agent architecture** where specialized AI agents work together to provide comprehensive Web3 security intelligence.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│  (React Frontend - Landing Page, Dashboard, Reports)        │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                      API Gateway                             │
│  (FastAPI - Authentication, Rate Limiting, Routing)         │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   Agent Orchestrator                         │
│  (Coordinates multi-agent workflows, manages state)         │
└─────────────────────┬───────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Threat Scout │ │  Phishing    │ │  Contract    │
│    Agent     │ │  Detector    │ │  Scanner     │
└──────────────┘ └──────────────┘ └──────────────┘
        │             │             │
        └─────────────┼─────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                    Xiaomi MiMo API                           │
│  (MiMo V2.5 for extraction, MiMo V2.5 Pro for reasoning)   │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   Data Layer                                 │
│  (PostgreSQL, Redis, S3 for reports)                        │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Frontend (React + TypeScript)

**Responsibilities**:
- Landing page with feature showcase
- User dashboard for threat monitoring
- Report viewer for detailed analysis
- Settings and preferences

**Tech Stack**:
- React 18 with TypeScript
- Tailwind CSS for styling
- Vite for build tooling
- Lucide React for icons

**Key Pages**:
- `/` - Landing page
- `/dashboard` - User dashboard (future)
- `/reports` - Report archive (future)
- `/docs` - Documentation (future)

### 2. API Gateway (FastAPI)

**Responsibilities**:
- Request authentication and authorization
- Rate limiting and quota management
- Request routing to appropriate agents
- Response formatting and caching

**Endpoints** (Planned):
```
POST /api/v1/scan/phishing
POST /api/v1/scan/contract
POST /api/v1/scan/rugpull
POST /api/v1/scan/tokenomics
GET  /api/v1/threats/daily
GET  /api/v1/reports/{report_id}
```

**Security**:
- JWT-based authentication
- API key management
- Rate limiting (100 req/hour free, 1000 req/hour pro)
- Input validation and sanitization

### 3. Agent Orchestrator

**Responsibilities**:
- Manages agent lifecycle
- Coordinates multi-agent workflows
- Handles agent communication
- Aggregates results

**Workflow Example** (Rugpull Detection):
```
1. User submits contract address
2. Orchestrator spawns:
   - Contract Scanner Agent (check code)
   - Tokenomics Analyst Agent (check distribution)
   - Social Trust Agent (check team)
3. Agents run in parallel
4. Orchestrator aggregates results
5. Report Generator Agent synthesizes findings
6. Final report returned to user
```

**State Management**:
- Redis for agent state
- PostgreSQL for persistent data
- In-memory cache for hot data

### 4. Specialized Agents

Each agent is a Python module with:
- **Input schema**: Defines expected inputs
- **Processing logic**: Core analysis algorithm
- **MiMo integration**: Calls to MiMo API
- **Output schema**: Structured results

#### Threat Scout Agent
```python
class ThreatScoutAgent:
    def __init__(self, mimo_client):
        self.mimo = mimo_client
        self.sources = [
            PhishingDatabaseAPI(),
            TwitterMonitor(),
            TelegramMonitor(),
            DiscordMonitor()
        ]
    
    async def scan(self) -> List[Threat]:
        # Collect data from sources
        raw_data = await self.collect_data()
        
        # Use MiMo V2.5 for extraction
        threats = await self.mimo.extract_threats(raw_data)
        
        # Use MiMo V2.5 Pro for risk scoring
        scored_threats = await self.mimo.score_threats(threats)
        
        return scored_threats
```

#### Phishing Detector Agent
```python
class PhishingDetectorAgent:
    def __init__(self, mimo_client):
        self.mimo = mimo_client
    
    async def analyze(self, url: str) -> PhishingReport:
        # Fetch page content
        content = await self.fetch_page(url)
        
        # Visual analysis
        screenshot = await self.capture_screenshot(url)
        visual_similarity = await self.compare_visuals(screenshot)
        
        # Domain analysis
        domain_info = await self.analyze_domain(url)
        
        # Use MiMo V2.5 Pro for reasoning
        risk_assessment = await self.mimo.assess_phishing_risk({
            "content": content,
            "visual_similarity": visual_similarity,
            "domain_info": domain_info
        })
        
        return PhishingReport(
            url=url,
            risk_score=risk_assessment.score,
            indicators=risk_assessment.indicators,
            recommendation=risk_assessment.recommendation
        )
```

#### Contract Scanner Agent
```python
class ContractScannerAgent:
    def __init__(self, mimo_client):
        self.mimo = mimo_client
    
    async def scan(self, address: str, chain: str) -> ContractReport:
        # Fetch contract code
        code = await self.fetch_contract_code(address, chain)
        
        # Static analysis
        vulnerabilities = await self.static_analysis(code)
        
        # Use MiMo V2.5 Pro for deep reasoning
        risk_analysis = await self.mimo.analyze_contract_risk({
            "code": code,
            "vulnerabilities": vulnerabilities,
            "chain": chain
        })
        
        return ContractReport(
            address=address,
            chain=chain,
            risk_score=risk_analysis.score,
            vulnerabilities=risk_analysis.vulnerabilities,
            recommendations=risk_analysis.recommendations
        )
```

### 5. Xiaomi MiMo Integration

**MiMo Client**:
```python
class MiMoClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.v25 = MiMoV25Client(api_key, base_url)
        self.v25_pro = MiMoV25ProClient(api_key, base_url)
    
    async def extract(self, text: str, schema: dict) -> dict:
        """Use MiMo V2.5 for extraction tasks"""
        return await self.v25.extract(text, schema)
    
    async def reason(self, context: dict, question: str) -> dict:
        """Use MiMo V2.5 Pro for reasoning tasks"""
        return await self.v25_pro.reason(context, question)
    
    async def synthesize(self, inputs: List[dict]) -> dict:
        """Use MiMo V2.5 Pro for multi-agent synthesis"""
        return await self.v25_pro.synthesize(inputs)
```

**Token Management**:
- Daily budget: 38M tokens
- Per-request limits: 500K tokens max
- Automatic retry with exponential backoff
- Fallback to cached results on quota exceeded

### 6. Data Layer

**PostgreSQL Schema**:
```sql
-- Threats table
CREATE TABLE threats (
    id UUID PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    severity VARCHAR(20) NOT NULL,
    detected_at TIMESTAMP NOT NULL,
    status VARCHAR(20) NOT NULL,
    data JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Reports table
CREATE TABLE reports (
    id UUID PRIMARY KEY,
    type VARCHAR(50) NOT NULL,
    threat_id UUID REFERENCES threats(id),
    content JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Users table (future)
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    tier VARCHAR(20) DEFAULT 'free',
    api_key VARCHAR(64) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

**Redis Cache**:
```
# Agent state
agent:{agent_id}:state -> JSON
agent:{agent_id}:last_run -> timestamp

# Rate limiting
ratelimit:{user_id}:hour -> counter
ratelimit:{user_id}:day -> counter

# Cached results
cache:phishing:{url_hash} -> JSON (TTL: 1 hour)
cache:contract:{address} -> JSON (TTL: 6 hours)
```

## Deployment Architecture

### Development
```
Local Machine
├── Frontend (Vite dev server)
├── Backend (FastAPI with hot reload)
└── PostgreSQL + Redis (Docker Compose)
```

### Production
```
Vercel (Frontend)
    │
    ▼
AWS ALB (Load Balancer)
    │
    ├─▶ ECS Fargate (API Gateway)
    ├─▶ ECS Fargate (Agent Workers)
    └─▶ Lambda (Scheduled tasks)
    │
    ▼
RDS PostgreSQL + ElastiCache Redis
    │
    ▼
S3 (Report storage)
```

## Scalability

### Horizontal Scaling
- **Frontend**: CDN + edge caching
- **API Gateway**: Auto-scaling ECS tasks
- **Agents**: Worker pool with task queue
- **Database**: Read replicas for queries

### Vertical Scaling
- **MiMo API**: Batch requests when possible
- **Caching**: Aggressive caching of common queries
- **Database**: Indexed queries, materialized views

### Cost Optimization
- **Token usage**: Cache results, batch requests
- **Compute**: Spot instances for non-critical tasks
- **Storage**: S3 lifecycle policies for old reports

## Security

### API Security
- HTTPS only
- JWT authentication
- API key rotation
- Rate limiting
- Input validation

### Data Security
- Encrypted at rest (RDS encryption)
- Encrypted in transit (TLS 1.3)
- No private keys or seed phrases stored
- Regular security audits

### Agent Security
- Sandboxed execution
- No external code execution
- Read-only blockchain access
- Human review for critical actions

## Monitoring

### Metrics
- Request latency (p50, p95, p99)
- Error rates by endpoint
- Token consumption by agent
- Agent success/failure rates

### Alerts
- High error rates (>5%)
- Token quota exceeded
- Agent failures
- Database connection issues

### Logging
- Structured JSON logs
- Centralized logging (CloudWatch)
- Log retention: 30 days
- PII redaction

## Future Enhancements

### Phase 2
- Real-time WebSocket alerts
- Mobile app (React Native)
- Browser extension (Chrome/Firefox)

### Phase 3
- On-chain monitoring (event listeners)
- Machine learning for pattern detection
- Community threat submissions

### Phase 4
- Decentralized threat database
- Token-based incentives
- DAO governance

---

**For more information**:
- [Application Description](./application_description.md)
- [MiMo Integration](./mimo_integration.md)
- [Token Consumption](./token_consumption.md)
