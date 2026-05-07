# TBAO Framework Overview / TBAO 框架概览

## What The Framework Is / 框架是什么

**English**: Trust-Bounded Agent OS (TBAO) is a public framework for keeping AI agent behavior bounded before it affects durable state, external systems, human judgment, or responsibility trails. It protects human meaning sovereignty and does not restrict intelligence growth; it restricts uncontrolled agent power.

**中文**：Trust-Bounded Agent OS（TBAO）是一个公开框架，用于在 AI Agent 影响长期状态、外部系统、人类判断或责任线索前保持边界。它保护人的意义主权，不限制智能生长，只限制失控的 Agent 权力。

## Three Governance Surfaces / 三类治理界面

**English**: TBAO is organized around three connected surfaces:

- **Knowledge Governance** preserves provenance, boundaries, confirmation status, and actionability of human knowledge.
- **Advisory Governance** makes judgment-shaping advice source-grounded, challengeable, verifiable, and downgradeable.
- **Action Governance** makes side-effectful action structured, risk-tiered, confirmable, traceable, and recoverable.

**中文**：TBAO 围绕三类相互连接的治理界面组织：

- **知识治理**：保留人的知识来源、边界、确认状态和可行动性。
- **顾问治理**：让影响判断的建议可溯源、可质疑、可校验、可降级。
- **行动治理**：让有外部副作用的行动结构化、风险分级、可确认、可追踪、可恢复。

## Action Spine As The First Demo Cut / Action Spine 作为第一演示切口

**English**: The current implementation focus is **Action Spine**, a minimal proposal structure for inspecting agent action before execution.

**中文**：当前实现焦点是 **Action Spine / 行动脊柱**，即在执行前检查 Agent 行动的最小提案结构。

```text
intent
  -> proposed_action
  -> risk_tier
  -> required_confirmation
  -> execution_status
  -> audit_note
```

**English**: v0.1 is mock-only. It has no execution, no runtime, no live API, no credentials, no real file writes, and no external side effects.

**中文**：v0.1 仅模拟；没有执行、没有运行时、没有实时 API、没有密钥、没有真实文件写入，也没有外部副作用。

## How To Read The Repository / 如何阅读仓库

**English**: Recommended reading path:

1. [`README.md`](../README.md)
2. [`docs/one-page-summary.zh-en.md`](one-page-summary.zh-en.md)
3. [`docs/framework-overview.zh-en.md`](framework-overview.zh-en.md)
4. [`docs/principles.zh-en.md`](principles.zh-en.md)
5. [`docs/action-spine-mvp.zh-en.md`](action-spine-mvp.zh-en.md)
6. [`docs/non-goals.zh-en.md`](non-goals.zh-en.md)
7. [`docs/development-log/action-spine-static-mock-example.md`](development-log/action-spine-static-mock-example.md)

**中文**：建议按以上顺序阅读：先看项目首页和一页摘要，再看框架概览、原则、Action Spine MVP、非目标，最后看静态模拟提案示例。

## Current Boundary / 当前边界

**English**: TBAO v0.1 is a public draft and non-production demo. It is local-only, mock-only, non-executing, and has no real credentials, no real funds, and no real external side effects.

**中文**：TBAO v0.1 是公开草稿和非生产演示。它仅本地、仅模拟、不执行，不使用真实密钥，不涉及真实资金，也不产生真实外部副作用。

## What Comes Next / 下一步

**English**: Phase 2 improves public narrative and navigation. Later phases may refine the static Action Spine demo and public release packaging, while preserving the non-production safety boundary unless a human explicitly approves a new scope.

**中文**：Phase 2 改进公共叙事和导航。后续阶段可以完善静态 Action Spine 演示和公开发布打包，但在人工明确批准新范围前，必须保留非生产安全边界。

## Final Test / 最终测试

**English**: Every future addition must answer:

```text
Does it protect human meaning sovereignty?
Does it preserve provenance, boundaries, and confirmation status?
Does it make judgment-shaping advice reviewable and downgradeable?
Does it make side-effectful action decidable, traceable, and recoverable?
```

**中文**：每一项未来新增内容都必须回答：

```text
它是否保护人的意义主权？
它是否保留来源、边界和确认状态？
它是否让影响判断的建议可审查、可降级？
它是否让有外部副作用的行动可裁决、可追踪、可恢复？
```

If not, it should not enter the TBAO main line.
