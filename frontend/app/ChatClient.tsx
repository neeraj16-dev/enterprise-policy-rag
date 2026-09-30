"use client";

import React, { useState, useRef, useEffect } from 'react';
import './chat.css';

interface Citation {
  chunk_id: string;
  policy_name: string;
  doc_ref: string;
  section: string;
  page: number;
  quote: string;
}

interface Verification {
  is_grounded: boolean;
  unsupported_claims: string[];
  hallucination_score: number;
  explanation: string;
  phantom_citations: string[];
}

interface RetrievedChunk {
  chunk_id: string;
  policy_name: string;
  doc_ref: string;
  page: number;
  section: string;
  content_preview: string;
}

interface Metrics {
  retrieval_rerank_ms: number;
  generation_ms: number;
  verification_ms: number;
  total_latency_ms: number;
}

interface ChatResponse {
  query: string;
  answer: string;
  citations: Citation[];
  verification: Verification;
  retrieved_chunks: RetrievedChunk[];
  metrics: Metrics;
}

interface Message {
  role: 'user' | 'bot';
  content: string;
  data?: ChatResponse;
}

export default function ChatClient({ pdfs }: { pdfs: string[] }) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [activeMetrics, setActiveMetrics] = useState<ChatResponse | null>(null);
  
  const [isAppLoading, setIsAppLoading] = useState(true);
  const [isServiceLoading, setIsServiceLoading] = useState(true);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  const presets = [
    "What time must company-issued assets be handed over to IT on the last working day?",
    "When does corporate Group Health Insurance coverage end after an employee leaves TechV-Flash?",
    "Can employees use PTO or Casual Leave while serving their notice period?",
    "Within how many days must employees submit their travel expense reports after completing a trip?"
  ];

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsAppLoading(false);
    }, 5000);
    return () => clearTimeout(timer);
  }, []);

  // Health check polling
  useEffect(() => {
    let intervalId: NodeJS.Timeout;

    const checkHealth = async () => {
      try {
        const res = await fetch('http://localhost:8000/health');
        if (res.status === 200) {
          setIsServiceLoading(false);
          clearInterval(intervalId);
        } else if (res.status === 503) {
          setIsServiceLoading(true);
        } else {
          // If it's another non-200, we'll keep it loading for now, 
          // or assume it's up if you prefer. The instructions said:
          // "once health check returns 200 or not 503 then stop calling"
          if (res.status !== 503) {
            setIsServiceLoading(false);
            clearInterval(intervalId);
          }
        }
      } catch (err) {
        setIsServiceLoading(true);
      }
    };

    // Initial check
    checkHealth();

    // Check every 5s
    intervalId = setInterval(checkHealth, 5000);

    return () => clearInterval(intervalId);
  }, []);


  const handleSubmit = async (e?: React.FormEvent) => {
    e?.preventDefault();
    if (!input.trim() || isLoading) return;

    const query = input.trim();
    setInput('');
    setMessages(prev => [...prev, { role: 'user', content: query }]);
    setIsLoading(true);

    try {
      // Assuming the backend is running locally on port 8000
      const response = await fetch('http://localhost:8000/api/v1/query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: query,
          top_n: 5,
          verify_grounding: true
        })
      });

      if (!response.ok) {
        throw new Error('Backend failed');
      }
      
      const data: ChatResponse = await response.json();
      setMessages(prev => [...prev, { role: 'bot', content: data.answer, data: data }]);
      setActiveMetrics(data);
      
    } catch (error) {
      console.error("Backend error:", error);
      setMessages(prev => [...prev, { role: 'bot', content: "cannot process your request at the moment. please try again later" }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  if (isAppLoading) {
    return (
      <div className="initial-loader-container">
        <div className="loader-logo">
          TechV<span style={{color: '#60a5fa'}}>-Flash</span>
        </div>
        <div className="loader-bars">
          <div className="bar"></div>
          <div className="bar"></div>
          <div className="bar"></div>
          <div className="bar"></div>
          <div className="bar"></div>
        </div>
        <div className="loader-text">INITIALIZING SECURE RAG PIPELINE...</div>
      </div>
    );
  }

  return (
    <div className="layout">
      {/* Left Panel */}
      <div className="panel left-panel">
        <div className="section-title">
          <i>✨</i> Quick Presets
        </div>
        <div className="preset-list">
          {presets.map((preset, idx) => (
            <button 
              key={idx} 
              className="preset-btn"
              onClick={() => setInput(preset)}
            >
              {preset}
            </button>
          ))}
        </div>

        <div className="section-title">
          <i>📚</i> Knowledge Corpus
        </div>
        <div className="pdf-grid">
          {pdfs.map((pdf, idx) => (
            <div key={idx} className="pdf-box" title={pdf}>
              <div className="pdf-icon">📄</div>
              <div className="pdf-name">{pdf.replace('TechV-Flash_', '').replace('.pdf', '').replace(/_/g, ' ')}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Center Panel - Chat UI */}
      <div className="panel center-panel" style={{ padding: 0 }}>
        {isServiceLoading && (
          <div className="service-banner">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
            Service is loading, please wait...
          </div>
        )}
        <div className="chat-header">
          <h1>TechV-Flash Assistant</h1>
        </div>
        
        <div className="chat-messages">
          {messages.length === 0 && (
            <div style={{ margin: 'auto', textAlign: 'center', color: '#94a3b8' }}>
              <div style={{ fontSize: '3rem', marginBottom: '16px' }}>🤖</div>
              <h2>How can I help you with enterprise policies today?</h2>
              <p style={{ marginTop: '8px' }}>Select a preset on the left or type your question below.</p>
            </div>
          )}
          
          {messages.map((msg, idx) => (
            <div key={idx} className={`message ${msg.role}`}>
              <div className="message-content">{msg.content}</div>
              
              {msg.data && msg.data.citations && msg.data.citations.length > 0 && (
                <div className="citations-box">
                  <strong>Sources:</strong>
                  <div>
                    {msg.data.citations.map((c, i) => (
                      <span key={i} className="citation-chip" title={c.quote}>
                        {c.policy_name} (Sec {c.section})
                      </span>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ))}
          
          {isLoading && (
            <div className="typing-indicator">
              <div className="typing-dot"></div>
              <div className="typing-dot"></div>
              <div className="typing-dot"></div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="chat-input-container">
          <form className="chat-input-wrapper" onSubmit={handleSubmit}>
            <textarea 
              className="chat-input"
              placeholder={isServiceLoading ? "Waiting for service..." : "Ask about TechV-Flash policies... (Press Enter to send)"}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              rows={1}
              disabled={isServiceLoading}
            />
            <button 
              type="submit" 
              className="send-btn"
              disabled={isLoading || !input.trim() || isServiceLoading}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
              </svg>
            </button>
          </form>
        </div>
      </div>

      {/* Right Panel - Metrics */}
      <div className="panel right-panel">
        <div className="section-title">
          <i>📊</i> Response Metrics
        </div>
        
        {!activeMetrics ? (
          <div style={{ textAlign: 'center', color: '#64748b', marginTop: '40px' }}>
            <div style={{ fontSize: '2rem', marginBottom: '16px' }}>⚡</div>
            <p>Submit a query to view RAG pipeline metrics and verification data.</p>
          </div>
        ) : (
          <div>
            <div className={`verify-card ${activeMetrics.verification.is_grounded ? '' : 'unverified'}`}>
              <div className="verify-header">
                <span style={{ fontSize: '1.5rem' }}>
                  {activeMetrics.verification.is_grounded ? '✅' : '⚠️'}
                </span>
                <span className="verify-status">
                  {activeMetrics.verification.is_grounded ? 'Grounded & Verified' : 'Needs Verification'}
                </span>
              </div>
              <div className="verify-score">
                {(1 - activeMetrics.verification.hallucination_score) * 100}% Confidence
              </div>
              <div className="verify-desc">
                {activeMetrics.verification.explanation}
              </div>
            </div>

            <div className="section-title" style={{ marginTop: '32px' }}>
              <i>⏱️</i> Latency Breakdown
            </div>
            
            <div className="metric-card">
              <div className="metric-label">
                <div className="metric-icon" style={{ color: '#8b5cf6' }}>🔍</div>
                Retrieval & Rerank
              </div>
              <div className="metric-value">
                {activeMetrics.metrics.retrieval_rerank_ms.toFixed(2)}<span className="ms">ms</span>
              </div>
            </div>
            
            <div className="metric-card">
              <div className="metric-label">
                <div className="metric-icon" style={{ color: '#ec4899' }}>🧠</div>
                Generation
              </div>
              <div className="metric-value">
                {activeMetrics.metrics.generation_ms.toFixed(2)}<span className="ms">ms</span>
              </div>
            </div>
            
            <div className="metric-card">
              <div className="metric-label">
                <div className="metric-icon" style={{ color: '#10b981' }}>🛡️</div>
                Verification
              </div>
              <div className="metric-value">
                {activeMetrics.metrics.verification_ms.toFixed(2)}<span className="ms">ms</span>
              </div>
            </div>
            
            <div className="metric-card" style={{ background: 'rgba(59, 130, 246, 0.1)', borderColor: 'rgba(59, 130, 246, 0.3)' }}>
              <div className="metric-label">
                <div className="metric-icon" style={{ color: '#3b82f6', background: 'rgba(59, 130, 246, 0.2)' }}>⚡</div>
                Total Latency
              </div>
              <div className="metric-value" style={{ color: '#60a5fa' }}>
                {activeMetrics.metrics.total_latency_ms.toFixed(2)}<span className="ms">ms</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
