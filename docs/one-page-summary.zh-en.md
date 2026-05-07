# Trust-Bounded Agent OS (TBAO)

## One-Sentence Summary / 一句话摘要

**English**: TBAO is a public framework and mock-only demo for making AI agent actions inspectable, bounded, confirmable, and auditable before execution.

**中文**：TBAO 是一个公开框架和仅模拟演示，用于让 AI Agent 的行动在执行前可检查、有边界、可确认、可审计。

## Why It Matters / 为什么重要

**English**: AI is moving from conversation to action across tools, files, APIs, workflows, and external systems. The critical risk is not only wrong answers, but uncontrolled agent power, unclear authority, missing confirmation, weak auditability, and unrecoverable side effects.

**中文**：AI 正在从对话走向跨工具、文件、API、工作流和外部系统的行动。关键风险不只是错误答案，还包括失控的 Agent 权力、模糊授权、缺失确认、弱审计能力和不可恢复的副作用。

## Core Position / 核心立场

**English**: TBAO protects human meaning sovereignty. It does not restrict the growth of intelligence; it restricts uncontrolled agent power. Agents may interpret and propose, but side-effectful action must be bounded and reviewable.

**中文**：TBAO 保护人的意义主权。它不限制智能的生长，只限制失控的 Agent 权力。Agent 可以解释和建议，但有外部副作用的行动必须有边界、可审查。

## Core Doctrine / 核心总纲

**English**

```text
1. Human beings retain sovereignty over meaning.
2. Human knowledge, experience, and preferences must retain provenance, boundaries, and confirmation status.
3. AI may interpret, advise, and act only within authorized boundaries.
4. Judgment-shaping advice must be source-grounded, challengeable, verifiable, and downgradeable.
5. Side-effectful action must be decidable, traceable, and recoverable.
```

**中文**

```text
1. 人拥有意义主权。
2. 人的知识、经验和偏好必须保留来源、边界和确认状态。
3. AI 只能在授权边界内解释、建议和行动。
4. 影响判断的建议必须可溯源、可质疑、可校验、可降级。
5. 有外部副作用的行动必须可裁决、可追踪、可恢复。
```

## Action Spine / 行动脊柱

```text
intent
  -> proposed_action
  -> risk_tier
  -> required_confirmation
  -> execution_status
  -> audit_note
```

**English**: Current v0.1 only demonstrates this structure as mock-only documentation. It does not execute actions or operate as a production runtime.

**中文**：当前 v0.1 只以仅模拟文档展示这个结构，不执行行动，也不是生产运行时。

## Governance Surfaces / 治理界面

**English**: TBAO uses three connected surfaces: **Knowledge Governance**, **Advisory Governance**, and **Action Governance**.

**中文**：TBAO 使用三个相互连接的治理界面：**知识治理**、**顾问治理**、**行动治理**。

## Current Status / 当前状态

**English**: v0.1 is a public draft. It includes a conceptual framework, governance spine, and mock-only Action Spine demo. It is not production-ready and includes no runtime execution, no live API, no scheduler, no worker, no real credentials, no real file writes, no real funds, and no external side effects.

**中文**：v0.1 是公开草稿，包含概念框架、治理脊柱和仅模拟的 Action Spine 演示。它尚非生产可用，不包含运行时执行、实时 API、调度器、worker、真实密钥、真实文件写入、真实资金或外部副作用。

## Who This Is For / 适合谁

**English**: AI agent builders, governance researchers, open-source tool designers, organizations exploring safe agent adoption, and individuals building personal AI workspaces.

**中文**：适合 AI Agent 构建者、治理研究者、开源工具设计者、探索安全 Agent 采用的组织，以及构建个人 AI 工作空间的个人。

## What This Is Not / TBAO 不是什么

**English**: TBAO is not a production runtime, not a general agent framework, not a content moderation system, not a claim that AI has conscience, and not a substitute for human responsibility, law, or institutional governance.

**中文**：TBAO 不是生产运行时，不是通用 Agent 框架，不是内容审核系统，不声称 AI 拥有良知，也不替代人的责任、法律或组织治理。

## Current Roadmap / 当前路线图

**English**

- Phase 1: completed collaboration baseline and static mock.
- Phase 2: public narrative and README framing.
- Phase 3: Action Spine static demo.
- Phase 4: public release packaging.

**中文**

- Phase 1：已完成协作基线和静态模拟。
- Phase 2：公共叙事和 README framing。
- Phase 3：Action Spine 静态演示。
- Phase 4：公开发布打包。

## Final Test / 最终测试

**English**

```text
Does it protect human meaning sovereignty?
Does it preserve provenance, boundaries, and confirmation status?
Does it make judgment-shaping advice reviewable and downgradeable?
Does it make side-effectful action decidable, traceable, and recoverable?
```

**中文**

```text
它是否保护人的意义主权？
它是否保留来源、边界和确认状态？
它是否让影响判断的建议可审查、可降级？
它是否让有外部副作用的行动可裁决、可追踪、可恢复？
```

**English**: Better agents do not only need more capability. They need trustworthy boundaries.

**中文**：更好的 Agent 不只需要更强能力，也需要可信边界。
