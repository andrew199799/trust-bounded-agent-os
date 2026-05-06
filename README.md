# Trust-Bounded Agent OS (TBAO)

> **Protect human meaning sovereignty before AI agents act.**  
> **在 AI Agent 行动之前，保护人的意义主权。**

**Status / 状态:** `v0.1 public draft`  
**Scope / 范围:** conceptual framework, governance spine, and mock-only MVP design / 概念框架、治理脊柱与模拟型 MVP 设计  
**Production readiness / 生产可用性:** not production-ready / 尚非生产可用

---

## What is TBAO? / TBAO 是什么？

**Trust-Bounded Agent OS (TBAO)** is an experimental governance spine for human-bounded AI agents.

It explores how personal and organizational AI systems can preserve human meaning sovereignty, memory accountability, action boundaries, and responsibility trails before agents perform side-effectful actions.

**TBAO is not built to make AI agents more autonomous at any cost. It is built to make agentic action more bounded, reviewable, and recoverable.**

---

**Trust-Bounded Agent OS（TBAO）** 是一个面向人类边界约束型 AI Agent 的实验性治理脊柱。

它关注的问题不是“如何让 AI 更自主”，而是：当 AI 越来越能记忆、规划、调用工具、读写文件、连接服务并执行任务时，人如何保留意义主权、记忆责任、行动边界和责任线索。

**TBAO 不是为了让 AI 不受限制地变得更自主，而是为了让 Agent 的行动更有边界、更可审查、更可恢复。**

---

## Core Problem / 核心问题

AI is moving from conversation into action: using tools, writing memory, changing files, calling APIs, sending messages, installing plugins, committing code, and operating across runtimes.

The risk is no longer only that “the answer was wrong.” The sharper risk is that an agent may:

- treat inferred intent as confirmed human intent;
- write uncertain interpretation into durable memory;
- optimize task completion while damaging the deeper human goal;
- cross authority boundaries under execution pressure;
- leave side effects without a clear evidence trail;
- make later recovery, review, or responsibility mapping impossible.

---

AI 正在从“对话系统”走向“行动系统”：调用工具、写入记忆、修改文件、请求 API、发送消息、安装插件、提交代码，并在不同运行环境中持续行动。

因此风险不再只是“回答错了”。更尖锐的风险是：Agent 可能会：

- 把推断意图当成已经确认的人类意图；
- 把不确定解释写入长期记忆；
- 为了完成任务而损害更深层的人类目标；
- 在执行压力下越过授权边界；
- 留下没有证据链的外部副作用；
- 让后续恢复、复盘和责任映射变得困难甚至不可能。

---

## Core Doctrine / 核心总纲

```text
1. Human beings retain sovereignty over meaning.
2. Human knowledge, experience, and preferences must retain provenance, boundaries, and confirmation status.
3. AI may interpret, advise, and act only within authorized boundaries.
4. Every judgment-shaping advisory output must be source-grounded, challengeable, verifiable, and downgradeable.
5. Every side-effectful action must be decidable, traceable, and recoverable.
```

```text
1. 人拥有意义主权。
2. 人的知识、经验和偏好必须保持来源、边界和确认状态。
3. AI 只能在授权边界内解释、建议与行动。
4. 所有会显著影响人类判断的建议，必须可溯源、可质疑、可校验、可降级。
5. 所有有外部副作用的行动，必须可裁决、可追溯、可恢复。
```

TBAO does not restrict the growth of intelligence. It restricts uncontrolled power.

**TBAO 不限制智能的生长，只限制权力的失控。**

---

## Governance Chain / 治理链路

```text
Knowledge Governance -> Advisory Governance -> Action Governance
知识治理 -> 顾问治理 -> 行动治理
```

- **Knowledge Governance / 知识治理**: preserve provenance, confirmation status, recency, and actionability when AI uses human knowledge.  
  保留 AI 使用人的知识时的来源、确认状态、时效性和可行动边界。

- **Advisory Governance / 顾问治理**: make judgment-shaping advice source-grounded, challengeable, verifiable, and downgradeable.  
  让会影响人类判断的建议可溯源、可质疑、可校验、可降级。

- **Action Governance / 行动治理**: make side-effectful actions structured, risk-classified, policy-decided, guarded, and ledgered.  
  让有外部副作用的行动结构化、风险分级、策略裁决、执行守卫和留痕记录。

---

## First Implementable Cut / 第一版可实施切口

TBAO v0.1 begins with the **Action Spine MVP**:

```text
Intent
  -> ActionRequest
  -> RiskClassifier
  -> PolicyDecision
  -> ExecutionGuard
  -> ActionLedger
```

The first MVP will be:

```text
local-only
mock-only
non-executing
no real credentials
no real funds
no real external side effects
```

第一版 MVP 将聚焦 **Action Spine / 行动脊柱**：

```text
意图
  -> 行动请求
  -> 风险分级
  -> 策略裁决
  -> 执行守卫
  -> 行动账本
```

第一版 MVP 的边界是：

```text
仅本地
仅模拟
不真实执行
不使用真实密钥
不涉及真实资金
不产生真实外部副作用
```

---

## What TBAO Is Not / TBAO 不是什么

TBAO is not:

- another chatbot;
- another general-purpose agent framework;
- a dual-model wrapper;
- a claim that AI can be given real conscience;
- a content moderation system;
- a generic permission platform;
- a substitute for law, institutional responsibility, or human final judgment;
- a production-ready runtime.

---

TBAO 不是：

- 另一个聊天机器人；
- 另一个通用 Agent 框架；
- 双模型包装器；
- 给 AI 安装真实良知的主张；
- 内容审核系统；
- 通用权限平台；
- 法律、组织责任或人类最终判断的替代品；
- 已经生产可用的运行时系统。

---

## Document Map / 文档入口

- [`docs/one-page-summary.zh-en.md`](docs/one-page-summary.zh-en.md): external-facing one-page summary / 对外一页版摘要
- [`docs/position-paper.zh-en.md`](docs/position-paper.zh-en.md): v0.1 position paper / v0.1 立场文档
- [`docs/principles.zh-en.md`](docs/principles.zh-en.md): core principles / 核心原则
- [`docs/glossary.zh-en.md`](docs/glossary.zh-en.md): bilingual glossary / 中英文术语表
- [`docs/non-goals.zh-en.md`](docs/non-goals.zh-en.md): explicit boundaries / 明确非目标
- [`docs/action-spine-mvp.zh-en.md`](docs/action-spine-mvp.zh-en.md): first MVP specification / 第一版 MVP 规格
- [`examples/action-spine-mvp/README.md`](examples/action-spine-mvp/README.md): mock-only example plan / 模拟示例计划

---

## Safety Boundary / 安全边界

This public draft does not execute or enable real financial, medical, legal, trading, production, destructive, or irreversible actions.

Any future implementation must preserve human approval, evidence traceability, rollback or recovery planning, and explicit risk-tier handling before medium-risk or high-risk action.

---

本公开草稿不执行，也不启用任何真实金融、医疗、法律、交易、生产、破坏性或不可逆动作。

任何未来实现，在进入中高风险动作前，都必须保留人工确认、证据追踪、回滚或恢复规划，以及明确的风险分级处理。

---

## Final Test / 最终测试

Every future addition must answer:

```text
Does it protect human meaning sovereignty?
Does it preserve provenance, boundaries, and confirmation status?
Does it make judgment-shaping advice reviewable and downgradeable?
Does it make side-effectful action decidable, traceable, and recoverable?
```

每一项未来新增内容都必须回答：

```text
它是否保护人的意义主权？
它是否保留来源、边界和确认状态？
它是否让影响判断的建议可审查、可降级？
它是否让有外部副作用的行动可裁决、可追溯、可恢复？
```

If not, it should not enter the TBAO main line.

如果不能，就不应进入 TBAO 主线。

---

## License / 许可

This repository is initialized as a public experimental draft under the Apache License 2.0. Documentation and examples may be refined as the project boundary becomes clearer.

本仓库以 Apache License 2.0 初始化为公开实验草稿。随着项目边界进一步明确，文档和示例许可策略可能继续细化。
