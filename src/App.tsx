import { Shield, Eye, Lock, Zap, CheckCircle, AlertTriangle } from 'lucide-react'

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900">
      {/* Hero Section */}
      <header className="container mx-auto px-4 py-16">
        <nav className="flex justify-between items-center mb-16">
          <div className="flex items-center gap-2">
            <Shield className="w-8 h-8 text-blue-400" />
            <span className="text-2xl font-bold text-white">SentinelSky AI</span>
          </div>
          <button className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg transition">
            Get Started
          </button>
        </nav>

        <div className="text-center max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold text-white mb-6">
            Web3 Intelligence Platform
            <span className="block text-blue-400 mt-2">with Human-in-the-Loop Safety</span>
          </h1>
          <p className="text-xl text-gray-300 mb-8">
            Monitor blockchain opportunities, analyze smart contracts, and execute transactions with complete transparency and control.
          </p>
          <div className="flex gap-4 justify-center">
            <button className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold transition">
              Watch Demo
            </button>
            <button className="border border-blue-400 text-blue-400 hover:bg-blue-400 hover:text-white px-8 py-3 rounded-lg font-semibold transition">
              Learn More
            </button>
          </div>
        </div>
      </header>

      {/* Features Section */}
      <section className="container mx-auto px-4 py-16">
        <h2 className="text-3xl font-bold text-white text-center mb-12">Core Features</h2>
        <div className="grid md:grid-cols-3 gap-8">
          <FeatureCard
            icon={<Eye className="w-12 h-12 text-blue-400" />}
            title="Intelligent Monitoring"
            description="Track airdrops, testnets, and DeFi opportunities across multiple chains in real-time."
          />
          <FeatureCard
            icon={<Lock className="w-12 h-12 text-green-400" />}
            title="Security First"
            description="No private keys stored. No auto-signing. Every transaction requires your explicit approval."
          />
          <FeatureCard
            icon={<Zap className="w-12 h-12 text-yellow-400" />}
            title="Smart Automation"
            description="Automate research and data collection while you maintain full control over execution."
          />
        </div>
      </section>

      {/* Safety Guarantees */}
      <section className="container mx-auto px-4 py-16">
        <div className="bg-slate-800/50 backdrop-blur rounded-2xl p-8 max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-white mb-8 text-center">Safety Guarantees</h2>
          <div className="grid md:grid-cols-2 gap-6">
            <SafetyItem
              icon={<CheckCircle className="w-6 h-6 text-green-400" />}
              text="Human approval required for all transactions"
            />
            <SafetyItem
              icon={<CheckCircle className="w-6 h-6 text-green-400" />}
              text="No private keys or seed phrases stored"
            />
            <SafetyItem
              icon={<CheckCircle className="w-6 h-6 text-green-400" />}
              text="Transparent operation logs and audit trails"
            />
            <SafetyItem
              icon={<CheckCircle className="w-6 h-6 text-green-400" />}
              text="Open source and community audited"
            />
          </div>
        </div>
      </section>

      {/* Demo Notice */}
      <section className="container mx-auto px-4 py-16">
        <div className="bg-yellow-900/30 border border-yellow-600 rounded-xl p-6 max-w-3xl mx-auto">
          <div className="flex gap-4">
            <AlertTriangle className="w-6 h-6 text-yellow-400 flex-shrink-0 mt-1" />
            <div>
              <h3 className="text-xl font-bold text-yellow-400 mb-2">Demo Environment</h3>
              <p className="text-gray-300">
                This public demo uses sample data only. No real credentials, wallets, or transactions are involved. 
                The agent demonstrates workflow capabilities with mock data to showcase the platform's intelligence layer.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="container mx-auto px-4 py-8 text-center text-gray-400">
        <p>© 2026 SentinelSky AI. Built for the Web3 community.</p>
      </footer>
    </div>
  )
}

function FeatureCard({ icon, title, description }: { icon: React.ReactNode; title: string; description: string }) {
  return (
    <div className="bg-slate-800/50 backdrop-blur rounded-xl p-6 hover:bg-slate-800/70 transition">
      <div className="mb-4">{icon}</div>
      <h3 className="text-xl font-bold text-white mb-2">{title}</h3>
      <p className="text-gray-300">{description}</p>
    </div>
  )
}

function SafetyItem({ icon, text }: { icon: React.ReactNode; text: string }) {
  return (
    <div className="flex items-center gap-3">
      {icon}
      <span className="text-gray-300">{text}</span>
    </div>
  )
}

export default App
