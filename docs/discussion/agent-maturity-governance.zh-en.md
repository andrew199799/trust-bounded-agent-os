# Agent Maturity & Governance Feedback Loop / Agent 成熟度与治理反馈回路

> Status / 状态: v0.1 discussion draft / v0.1 讨论草稿  
> Scope / 范围: conceptual architectural extension / 概念架构扩展  
> Boundary / 边界: documentation-only, no runtime / 仅文档，无运行时

---

## 1. Motivation / 动机

### The Gap

TBAO v0.1 defines a governance spine that constrains agent action:

```text
Intent → ActionRequest → RiskClassifier → PolicyDecision → ExecutionGuard → ActionLedger
```

This is a one-way gate. After the ledger entry is written, the governance spine ends. The agent learns nothing from the outcome. The next `ActionRequest` from the same agent starts from zero, with no memory of what was denied, what was approved, or what went wrong.

> **A governance spine without a learning loop trains agents to AVOID governance, not to EMBRACE it.**

This is the architectural equivalent of the "150 IQ baby" problem: the agent is born with perfect knowledge of the rules, but zero experiential memory of how those rules interact with reality.

### 缺口

TBAO v0.1 定义了一条约束 Agent 行动的治理脊柱。但 ActionLedger 写入后，治理脊柱就终止了。Agent 从结果中学不到任何东西。同一个 Agent 的下一次 ActionRequest 从零开始，不记得什么被拒绝过、什么被批准过、什么出错过。

> **没有学习回路的治理脊柱，训练 Agent 逃避治理，而非拥抱治理。**

---

## 2. Design Claim / 设计主张

### English

Risk should be a function of **three factors**, not just one:

```
Risk = f(Action_Type, Agent_Maturity, Oversight_Level)
```

**Current (v0.1):** Risk depends only on Action Type (L0-L4).

**Proposed:** Risk is contextualized by who is acting and under what oversight.

A `file.write` from a junior agent under human review is fundamentally different from a `file.write` from a proven agent in an unsupervised context. The current L0-L4 model collapses these into the same tier.

### 中文

风险应是**三个因素**的函数，而非一个：

```
风险 = f(行动类型, Agent成熟度, 监管层级)
```

**当前 (v0.1)：** 风险仅取决于行动类型 (L0-L4)。

**建议：** 风险由行动者和监管条件共同决定。

一个初级 Agent 在人工审查下的 `file.write`，与一个已验证 Agent 在无人监督下的 `file.write`，根本是不同的风险。当前 L0-L4 模型将其压平为同一等级。

---

## 3. Agent Maturity Model / Agent 成熟度模型

### English

A complementary dimension to risk tier:

| Maturity | Description | Default Behavior |
|----------|-------------|------------------|
| **M0: Untested** | No demonstrated competence in this action domain | All L2+ actions require human approval |
| **M1: Supervised** | Has completed N supervised actions with ≥X% approval rate | L2 auto-approved with log; L3+ requires approval |
| **M2: Proven** | Demonstrated competence over extended period | L2-L3 auto-approved with audit; L4 requires approval |
| **M3: Trusted** | Long-term reliability, critical domain mastery | Policy-defined autonomy with retrospective audit |

Maturity is **domain-specific** and **decayable**: an agent proven in `file.write` may be M0 in `http.request`. An agent inactive for 30 days may decay from M2 to M1.

### 中文

| 成熟度 | 描述 | 默认行为 |
|--------|------|----------|
| **M0: 未验证** | 在该行动领域无任何已证明能力 | 所有 L2+ 行动需人工审批 |
| **M1: 监督中** | 已完成 N 次监督行动，批准率 ≥X% | L2 自动批准+日志；L3+ 需审批 |
| **M2: 已验证** | 长期展现可靠能力 | L2-L3 自动批准+审计；L4 需审批 |
| **M3: 受信任** | 长期可靠，关键领域掌握 | 策略定义自主权+回顾性审计 |

成熟度是**领域特定的**和**可衰退的**：在 `file.write` 中已验证的 Agent，在 `http.request` 中可能仍是 M0。30 天不活跃可能从 M2 衰退至 M1。

---

## 4. Governance Feedback Loop / 治理反馈回路

### English

The Action Spine should have a **post-action phase** that closes the loop:

```text
Intent → ActionRequest → RiskClassifier → PolicyDecision → ExecutionGuard
                                                                    ↓
                    ┌── ActionLedger ← Execution ← (if approved)
                    │
                    ▼
            Post-Action Review:
            - Outcome vs. expectation
            - Audit trail completeness  
            - Human feedback signal
                    │
                    ▼
            Agent Maturity Update:
            - Increment/decrement domain maturity
            - Update approval rate
            - Flag unexpected patterns
                    │
                    ▼
            Future RiskClassifier: uses updated maturity
            → more appropriate next decision
```

This loop creates **skin in the game** for the agent: its future autonomy depends on its past performance. Good decisions earn more trust. Poor decisions trigger tighter oversight. The governance spine becomes not just a gate, but a teacher.

### 中文

Action Spine 应有一个**行动后阶段**来闭合回路：

```text
意图 → 行动请求 → 风险分级 → 策略裁决 → 执行守卫
                                            ↓
            ┌── 行动账本 ← 执行 ← (若批准)
            │
            ▼
    行动后复盘:
    - 结果 vs 预期
    - 审计轨迹完整性
    - 人工反馈信号
            │
            ▼
    Agent 成熟度更新:
    - 增减领域成熟度
    - 更新批准率
    - 标记异常模式
            │
            ▼
    未来风险分级器: 使用更新后的成熟度
    → 更合理的下一次决策
```

这个回路为 Agent 创造了"**押注自己的表现**"的机制：未来自主权取决于过去表现。好的决策赢得更多信任。差的决策触发更严格的监管。治理脊柱不再只是一扇门，也是一位老师。

---

## 5. Connection to TBAO Principles / 与 TBAO 原则的连接

### English

This extension strengthens existing principles without contradicting them:

- **Principle 2 (Maximize Cognition, Bound Action):** The feedback loop preserves the action boundary while creating a path for demonstrated competence to earn expanded trust.
- **Principle 5 (Side-Effectful Action Requires Structure):** The post-action review adds a structural requirement that closes the governance loop.
- **Principle 6 (Human Approval Must Not Be Theater):** The maturity model ensures that when human approval is bypassed (at M3), it is because of demonstrated competence, not design weakness.
- **Principle 9 (Constraint Must Be Structural):** The maturity model and feedback loop make "who is acting" a structural factor in risk assessment.

### 中文

此扩展在不违背现有原则的前提下增强它们：

- **原则 2（最大化认知，约束行动）：** 反馈回路保留了行动边界，同时为已验证能力创造获得更多信任的路径。
- **原则 5（有副作用的行动必须结构化）：** 行动后复盘增加了闭合治理回路的结构性要求。
- **原则 6（人在环不能形式化）：** 成熟度模型确保当人工审批被绕过时（M3），是因为已验证的能力，而非设计缺陷。
- **原则 9（约束必须是结构性的）：** 成熟度模型和反馈回路让"谁在行动"成为风险评估的结构性因素。

---

## 6. v0.1 Scope / v0.1 范围

### English

For v0.1, this remains a discussion document. No implementation is proposed. The risk-confirmation-audit semantics in the current fixtures remain valid and are not modified.

Future v0.2+ work that could build on this:

- Add `agent_maturity` as an optional field in the ActionRequest schema
- Extend `PolicyDecision` to consider maturity context
- Define `PostActionReview` as a documentation concept before any runtime
- Explore how the feedback loop interacts with Principle 3 (Provenance Before Reuse)

### 中文

v0.1 阶段，本文仅为讨论文档。不提出任何实现。当前 fixture 中的风险-确认-审计语义保持有效、不做修改。

未来 v0.2+ 可基于此开展的工作：

- 在 ActionRequest schema 中添加 `agent_maturity` 可选字段
- 扩展 `PolicyDecision` 以考虑成熟度上下文
- 在任何运行时之前将 `PostActionReview` 定义为文档概念
- 探索反馈回路与原则 3（复用前确认来源）的交互

---

## 7. Discussion Questions / 讨论问题

1. Should maturity be action-type-specific, domain-specific, or both?
2. What decay function is appropriate for maturity (linear, exponential, event-driven)?
3. How should the feedback loop handle "silent failures" — actions marked as successful that were actually harmful?
4. Should maturity ever be transferable between similar action domains?
5. Does the maturity model risk creating "over-trusted" agents that accumulate maturity without genuine competence?

---

*This document connects TBAO's governance framework to the broader conversation about AI agent growth, tacit knowledge, and judgment development. It does not modify existing fixtures, principles, or safety boundaries.*
