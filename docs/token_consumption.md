# Token Consumption Model

## Overview

SentinelSky AI uses Xiaomi MiMo models extensively for Web3 security intelligence. This document details our token consumption model, optimization strategies, and projected usage at scale.

## Model Selection Strategy

### MiMo V2.5 (Standard)
**Use Cases**:
- Text summarization
- Data extraction from structured sources
- Multilingual translation
- Pattern matching
- Simple classification

**Characteristics**:
- Lower token cost
- Faster response time
- Suitable for high-volume tasks
- Good for deterministic outputs

### MiMo V2.5 Pro (Advanced)
**Use Cases**:
- Deep risk reasoning
- Smart contract vulnerability analysis
- Multi-factor risk scoring
- Complex pattern detection
- Multi-agent result synthesis

**Characteristics**:
- Higher token cost
- Superior reasoning capability
- Required for critical decisions
- Better context understanding

## Agent Token Consumption

### Daily Usage Breakdown

| Agent | Model | Tokens/Run | Runs/Day | Daily Tokens | Monthly Tokens |
|---|---|---:|---:|---:|---:|
| **Threat Scout Agent** | V2.5 | 120,000 | 24 | 2,880,000 | 86,400,000 |
| **Phishing Detector Agent** | V2.5 Pro | 180,000 | 30 | 5,400,000 | 162,000,000 |
| **Contract Scanner Agent** | V2.5 Pro | 450,000 | 20 | 9,000,000 | 270,000,000 |
| **Rugpull Risk Agent** | V2.5 Pro | 350,000 | 20 | 7,000,000 | 210,000,000 |
| **Tokenomics Analyst Agent** | V2.5 Pro | 300,000 | 15 | 4,500,000 | 135,000,000 |
| **Social Trust Agent** | V2.5 | 150,000 | 20 | 3,000,000 | 90,000,000 |
| **Report Generator Agent** | V2.5 | 250,000 | 10 | 2,500,000 | 75,000,000 |
| **Multilingual Threat Research** | V2.5 | 250,000 | 15 | 3,750,000 | 112,500,000 |
| **TOTAL** | | | | **38,030,000** | **1,140,900,000** |

### Token Consumption Details

#### 1. Threat Scout Agent (120K tokens/run)
```
Input Context:
- Phishing database feeds (20K tokens)
- Twitter/Telegram monitoring (30K tokens)
- Domain registration data (15K tokens)

Processing:
- Extract threat indicators (MiMo V2.5)
- Classify threat types
- Generate threat summaries

Output:
- Structured threat list (5K tokens)
- Daily digest report (50K tokens)

Total: ~120K tokens per run
Runs: 24 times/day (hourly monitoring)
Daily: 2.88M tokens
```

#### 2. Phishing Detector Agent (180K tokens/run)
```
Input Context:
- URL and domain info (10K tokens)
- Page content and HTML (40K tokens)
- Visual similarity analysis (20K tokens)
- WHOIS and DNS records (10K tokens)

Processing:
- Deep risk reasoning (MiMo V2.5 Pro)
- Multi-factor risk scoring
- Indicator correlation

Output:
- Detailed phishing report (100K tokens)

Total: ~180K tokens per run
Runs: 30 times/day (on-demand + scheduled)
Daily: 5.4M tokens
```

#### 3. Contract Scanner Agent (450K tokens/run)
```
Input Context:
- Smart contract source code (150K tokens)
- Bytecode analysis (50K tokens)
- Transaction history (30K tokens)
- Similar contract patterns (40K tokens)

Processing:
- Vulnerability detection (MiMo V2.5 Pro)
- Risk reasoning and scoring
- Exploit scenario generation

Output:
- Comprehensive security report (180K tokens)

Total: ~450K tokens per run
Runs: 20 times/day (on-demand)
Daily: 9M tokens
```

#### 4. Rugpull Risk Agent (350K tokens/run)
```
Input Context:
- Token contract code (100K tokens)
- Liquidity pool data (30K tokens)
- Holder distribution (20K tokens)
- Team and social data (40K tokens)

Processing:
- Multi-factor risk analysis (MiMo V2.5 Pro)
- Historical pattern matching
- Probability scoring

Output:
- Rugpull risk report (160K tokens)

Total: ~350K tokens per run
Runs: 20 times/day (on-demand)
Daily: 7M tokens
```

#### 5. Tokenomics Analyst Agent (300K tokens/run)
```
Input Context:
- Token distribution data (40K tokens)
- Vesting schedules (30K tokens)
- Inflation/deflation mechanisms (30K tokens)
- Competitor comparison (40K tokens)

Processing:
- Economic modeling (MiMo V2.5 Pro)
- Risk assessment
- Projection calculations

Output:
- Tokenomics analysis report (160K tokens)

Total: ~300K tokens per run
Runs: 15 times/day (on-demand)
Daily: 4.5M tokens
```

#### 6. Social Trust Agent (150K tokens/run)
```
Input Context:
- Twitter/Telegram/Discord data (60K tokens)
- Team background research (20K tokens)
- Community sentiment (15K tokens)

Processing:
- Pattern detection (MiMo V2.5)
- Bot identification
- Reputation scoring

Output:
- Social trust report (55K tokens)

Total: ~150K tokens per run
Runs: 20 times/day (continuous monitoring)
Daily: 3M tokens
```

#### 7. Report Generator Agent (250K tokens/run)
```
Input Context:
- All agent findings (150K tokens)
- Historical context (30K tokens)

Processing:
- Multi-agent synthesis (MiMo V2.5)
- Report formatting
- Recommendation generation

Output:
- Final comprehensive report (70K tokens)

Total: ~250K tokens per run
Runs: 10 times/day (daily digests + on-demand)
Daily: 2.5M tokens
```

#### 8. Multilingual Threat Research (250K tokens/run)
```
Input Context:
- Non-English threat sources (100K tokens)
- Translation context (30K tokens)

Processing:
- Multilingual extraction (MiMo V2.5)
- Cross-language threat correlation
- Translation and localization

Output:
- Translated threat intelligence (120K tokens)

Total: ~250K tokens per run
Runs: 15 times/day (covering major languages)
Daily: 3.75M tokens
```

## Scaling Projections

### Single Instance (Current)
```
Daily:   38M tokens
Monthly: 1.14B tokens
Yearly:  13.9B tokens
```

### Community Scale (100 users)
```
Daily:   380M tokens
Monthly: 11.4B tokens
Yearly:  139B tokens
```

### Production Scale (1,000 users)
```
Daily:   3.8B tokens
Monthly: 114B tokens
Yearly:  1.39T tokens
```

### Enterprise Scale (10,000 users)
```
Daily:   38B tokens
Monthly: 1.14T tokens
Yearly:  13.9T tokens
```

**Note**: Community scale can exceed **5B tokens/month** with shared threat intelligence and collaborative monitoring.

## Optimization Strategies

### 1. Intelligent Caching
```python
# Cache phishing detection results
cache_key = f"phishing:{url_hash}"
cached_result = redis.get(cache_key)
if cached_result and age < 1_hour:
    return cached_result

# Fresh analysis
result = await phishing_agent.analyze(url)
redis.setex(cache_key, 3600, result)
```

**Savings**: 30-40% reduction in duplicate analyses

### 2. Batch Processing
```python
# Batch similar requests
batch = collect_pending_requests(max_size=10, max_wait=5)
results = await mimo.batch_analyze(batch)
```

**Savings**: 20-25% reduction through context sharing

### 3. Incremental Updates
```python
# Only analyze changes since last scan
last_scan = get_last_scan(contract_address)
changes = detect_changes(contract_address, last_scan)
if not changes:
    return cached_report

# Incremental analysis
result = await contract_agent.analyze_changes(changes)
```

**Savings**: 40-50% reduction for repeat scans

### 4. Tiered Analysis
```python
# Quick scan first (MiMo V2.5)
quick_result = await quick_scan(url)
if quick_result.risk_score < 50:
    return quick_result

# Deep analysis only for high-risk (MiMo V2.5 Pro)
deep_result = await deep_scan(url)
return deep_result
```

**Savings**: 25-30% reduction by avoiding unnecessary deep scans

### 5. Result Sharing
```python
# Share results across users
if is_public_threat(url):
    # One analysis benefits all users
    result = get_or_create_analysis(url)
    return result
```

**Savings**: 60-70% reduction through community sharing

## Cost Analysis

### Token Pricing (Estimated)
```
MiMo V2.5:     $0.50 per 1M tokens
MiMo V2.5 Pro: $2.00 per 1M tokens
```

### Daily Cost (Single Instance)
```
V2.5 usage:     12.13M tokens × $0.50 = $6.07
V2.5 Pro usage: 25.90M tokens × $2.00 = $51.80
Total daily:    $57.87
Total monthly:  $1,736
```

### Monthly Cost by Scale
```
Single instance:  $1,736
100 users:        $17,360 (with 40% optimization: $10,416)
1,000 users:      $173,600 (with 60% optimization: $69,440)
10,000 users:     $1,736,000 (with 70% optimization: $520,800)
```

### Revenue Model
```
Free tier:  $0/month (limited to daily digest)
Pro tier:   $29/month (full access)
Enterprise: $499/month (white-label + SLA)

Break-even: 60 Pro users or 4 Enterprise customers
```

## Token Budget Management

### Daily Budget: 38M tokens
```python
class TokenBudgetManager:
    def __init__(self):
        self.daily_budget = 38_000_000
        self.used_today = 0
        self.reset_time = get_next_midnight()
    
    async def request_tokens(self, agent: str, amount: int) -> bool:
        if self.used_today + amount > self.daily_budget:
            # Quota exceeded
            if is_critical_request():
                # Allow critical requests
                return True
            else:
                # Defer non-critical requests
                await queue_for_tomorrow(agent, amount)
                return False
        
        self.used_today += amount
        return True
```

### Priority System
```
Priority 1 (Critical): Rugpull detection, contract vulnerabilities
Priority 2 (High):     Phishing detection, threat monitoring
Priority 3 (Medium):   Tokenomics analysis, social trust
Priority 4 (Low):      Report generation, translations
```

## Monitoring and Alerts

### Token Usage Metrics
```
- Tokens used per agent per day
- Tokens used per user per day
- Average tokens per request
- Token efficiency (results per token)
```

### Alerts
```
- Daily budget 80% consumed
- Unusual spike in token usage
- Agent token usage anomaly
- Quota exceeded events
```

## Future Optimizations

### Phase 2
- Fine-tuned models for specific tasks
- Prompt engineering optimization
- Context compression techniques

### Phase 3
- Local model deployment for simple tasks
- Hybrid cloud/edge architecture
- Federated learning for pattern detection

### Phase 4
- Custom MiMo model training
- Domain-specific model optimization
- Zero-shot learning for new threats

## Conclusion

SentinelSky AI's token consumption model is designed for:
- **Efficiency**: Intelligent caching and batching
- **Scalability**: Linear scaling with optimizations
- **Sustainability**: Revenue model supports token costs
- **Quality**: Right model for each task

With **38M tokens/day** for comprehensive coverage and **5B+ tokens/month** at community scale, SentinelSky AI demonstrates the power of Xiaomi MiMo for real-world Web3 security applications.

---

**For more information**:
- [Application Description](./application_description.md)
- [Architecture](./architecture.md)
- [MiMo Integration](./mimo_integration.md)
