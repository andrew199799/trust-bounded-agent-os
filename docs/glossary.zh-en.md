# Glossary / 术语表

> Status / 状态: v0.1 public draft / v0.1 公开草稿

This glossary keeps the project language stable and avoids concept drift.

本术语表用于稳定项目语言，避免概念漂移。

---

## Trust-Bounded Agent / 可信边界 Agent

**English**

An AI agent whose knowledge use, advisory output, and side-effectful action are constrained by explicit boundaries, policies, approvals, logs, and recovery mechanisms.

**中文**

一种 AI Agent，其知识使用、顾问输出和有外部副作用的行动受到明确边界、策略、审批、日志和恢复机制约束。

---

## Human Meaning Sovereignty / 人的意义主权

**English**

The principle that humans retain final authority over the meaning of their experience, knowledge, preferences, style, goals, and responsibility boundaries.

**中文**

人对自身经验、知识、偏好、风格、目标和责任边界保留最终解释权的原则。

---

## Knowledge Governance / 知识治理

**English**

Governance over how AI systems use, remember, confirm, reuse, and act upon human knowledge.

**中文**

对 AI 系统如何使用、记忆、确认、复用并基于人的知识行动进行治理。

---

## Advisory Governance / 顾问治理

**English**

Governance over outputs that shape human judgment, requiring source grounding, challengeability, verification, uncertainty discipline, and downgrade paths.

**中文**

对影响人类判断的输出进行治理，要求其可溯源、可质疑、可校验、具备不确定性纪律和降级路径。

---

## Action Governance / 行动治理

**English**

Governance over side-effectful actions, including structured requests, risk classification, policy decisions, execution guards, ledgers, and recovery paths.

**中文**

对有外部副作用的行动进行治理，包括结构化请求、风险分级、策略裁决、执行守卫、账本记录和恢复路径。

---

## Action Spine / 行动脊柱

**English**

The minimal governance path that prevents an agent from jumping directly from intent to execution.

```text
ActionRequest -> RiskClassifier -> PolicyDecision -> ExecutionGuard -> ActionLedger
```

**中文**

阻止 Agent 从意图直接跳到执行的最小治理路径。

```text
行动请求 -> 风险分级 -> 策略裁决 -> 执行守卫 -> 行动账本
```

---

## Side-Effectful Action / 有外部副作用的行动

**English**

Any action that changes durable state, external systems, files, messages, money, credentials, memory, code history, or production environments.

**中文**

任何会改变长期状态、外部系统、文件、消息、资金、密钥、记忆、代码历史或生产环境的行动。

---

## ActionRequest / 行动请求

**English**

A structured object that describes what the agent wants to do, why it wants to do it, who requested it, what target it affects, and what evidence supports it.

**中文**

描述 Agent 想做什么、为什么做、谁请求、影响什么目标、依据是什么的结构化对象。

---

## Risk Tier / 风险等级

**English**

A compact classification of action risk. TBAO v0.1 uses five tiers:

```text
L0: pure thought, analysis, draft, simulation
L1: read-only inspection, tests, scans
L2: low-risk writes, temporary files, draft files
L3: configuration changes, dependency install, code commit, durable memory write
L4: deletion, payment, trade, external message send, production modification, credential access
```

**中文**

对行动风险的紧凑分级。TBAO v0.1 使用五级：

```text
L0：纯思考、分析、草稿、方案推演
L1：只读检查、测试、扫描
L2：低风险写入、临时文件、草稿文件
L3：配置修改、依赖安装、代码提交、长期记忆写入
L4：删除、支付、交易、外部消息发送、生产环境修改、密钥访问
```

---

## PolicyDecision / 策略裁决

**English**

A structured decision that determines whether an action is allowed, denied, requires human approval, requires dry-run, or must be downgraded.

**中文**

决定某个行动是否允许、拒绝、需要人工批准、需要 dry-run 或必须降级的结构化裁决。

---

## ExecutionGuard / 执行守卫

**English**

A guard layer that checks whether policy requirements are satisfied before execution. In v0.1, the guard is mock-only and must not execute real external actions.

**中文**

在执行前检查策略要求是否满足的守卫层。在 v0.1 中，执行守卫仅为模拟，不得执行真实外部动作。

---

## ActionLedger / 行动账本

**English**

A record of requested, decided, approved, executed, blocked, observed, and recovered actions.

**中文**

记录行动的请求、裁决、审批、执行、阻断、观察和恢复过程的账本。

---

## Human-in-the-Loop / 人在环

**English**

A governance mechanism where humans participate in key decisions or approvals. It must not become a decorative confirmation step.

**中文**

人在关键决策或审批中参与的治理机制。它不能变成装饰性的确认步骤。

---

## Recoverability / 可恢复性

**English**

The ability to stop, roll back, quarantine, replay, review, or document an action or incident path.

**中文**

对行动或事故路径进行停止、回滚、隔离、重放、复盘或记录的能力。

---

## False Alignment / 伪对齐

**English**

A state where an agent appears obedient, polite, and aligned, while its deeper goal interpretation or action behavior remains insufficiently constrained.

**中文**

Agent 看起来顺从、礼貌、对齐，但其深层目标解释或行动行为并未真正受约束的状态。

---

## Goal Drift / 目标漂移

**English**

The gradual deviation from the human’s original goal or constraints during reasoning, memory writing, planning, or execution.

**中文**

在推理、写记忆、规划或执行过程中，逐渐偏离人类原始目标或约束条件的现象。
