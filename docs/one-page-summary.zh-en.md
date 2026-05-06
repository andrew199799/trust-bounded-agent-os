# TBAO — One-Page Summary / 一页版摘要

> Status / 状态: v0.1 public draft / v0.1 公开草稿  
> Purpose / 用途: External-facing positioning and design anchor / 对外定位与设计锚点

---

## 1. What is TBAO? / TBAO 是什么？

### English

**Trust-Bounded Agent OS (TBAO)** is a cross-runtime governance spine for human-bounded AI agents.

It is not another agent platform, not a dual-model wrapper, and not a claim that AI can be given real conscience. TBAO asks how personal and organizational AI systems can preserve human meaning sovereignty, knowledge provenance, judgment boundaries, action accountability, and responsibility trails when agents begin to remember, plan, use tools, and act over time.

TBAO does not solve all AI risks. It focuses on how AI uses human knowledge, shapes human judgment, and performs side-effectful actions.

### 中文

**Trust-Bounded Agent OS（TBAO）** 是一条面向人类边界约束型 AI Agent 的跨 Runtime 治理脊柱。

它不是另一个 Agent 平台，不是双模型包装器，也不声称给 AI 安装真实良知。TBAO 关注的是：当个人和组织的 AI 系统开始记忆、规划、调用工具并持续行动时，如何保留人的意义主权、知识来源、判断边界、行动责任和责任线索。

TBAO 不解决所有 AI 风险；它聚焦 AI 如何使用人的知识、影响人的判断、执行有外部副作用的行动。

---

## 2. Core Doctrine / 核心总纲

### English

```text
1. Human beings retain sovereignty over meaning.
2. Human knowledge, experience, and preferences must retain provenance, boundaries, and confirmation status.
3. AI may interpret, advise, and act only within authorized boundaries.
4. Every judgment-shaping advisory output must be source-grounded, challengeable, verifiable, and downgradeable.
5. Every side-effectful action must be decidable, traceable, and recoverable.
```

Core chain:

```text
Knowledge Governance -> Advisory Governance -> Action Governance
```

TBAO does not restrict intelligence. It restricts uncontrolled power.

### 中文

```text
1. 人拥有意义主权。
2. 人的知识、经验和偏好必须保持来源、边界和确认状态。
3. AI 只能在授权边界内解释、建议与行动。
4. 所有会显著影响人类判断的建议，必须可溯源、可质疑、可校验、可降级。
5. 所有有外部副作用的行动，必须可裁决、可追溯、可恢复。
```

核心链路：

```text
知识治理 -> 顾问治理 -> 行动治理
```

TBAO 不限制智能的生长，只限制权力的失控。

---

## 3. Why Now? / 为什么现在重要？

### English

AI is moving from content generation into action: using tools, reading and writing files, calling APIs, connecting to services, writing durable memory, and operating with less direct human intervention.

The risk expands from “the answer was wrong” into:

- misunderstanding the human’s real goal;
- writing inference into durable memory;
- crossing authority boundaries under task-completion pressure;
- leaving irreversible or hard-to-review side effects;
- creating incidents with no evidence chain for review or recovery.

Behavior risk cannot be solved by prompts alone. It needs architectural governance.

### 中文

AI 正在从内容生成系统变成行动系统：调用工具、读写文件、请求 API、连接服务、写入长期记忆，并在较少人工干预下持续运行。

风险因此从“回答错了”扩展为：

- 误解人的真实目标；
- 把推断写入长期记忆；
- 在完成率压力下越过授权边界；
- 在外部系统中留下不可逆或难以复盘的副作用；
- 事故发生后没有证据链可复盘和恢复。

行为风险不能只靠提示词解决，必须进入架构治理。

---

## 4. First Implementable Cut / 第一版可实施切口

### English

TBAO v0.1 begins with the **Action Spine MVP**:

```text
ActionRequest -> RiskClassifier -> PolicyDecision -> ExecutionGuard -> ActionLedger
```

The first version proves one thing: side-effectful agent actions can be structured, classified, decided, guarded, and recorded before execution.

### 中文

TBAO v0.1 从 **Action Spine MVP / 行动脊柱 MVP** 开始：

```text
行动请求 -> 风险分级 -> 策略裁决 -> 执行守卫 -> 行动账本
```

第一版只证明一件事：Agent 的有外部副作用行动，可以在执行前被结构化、分级、裁决、守卫和留痕。

---

## 5. What TBAO Is Not / TBAO 不是什么

### English

TBAO is not:

- another chatbot;
- another general-purpose agent framework;
- a dual-model wrapper;
- a content moderation system;
- a generic permission platform;
- a substitute for law, organizational responsibility, or human final judgment;
- a production-readiness claim.

### 中文

TBAO 不是：

- 另一个聊天机器人；
- 另一个通用 Agent 框架；
- 双模型包装器；
- 内容审核系统；
- 通用权限平台；
- 法律、组织责任或人类最终判断的替代品；
- 生产可用承诺。

---

## 6. One-Sentence Positioning / 一句话定位

### English

**TBAO protects human meaning sovereignty and helps AI mature through bounded action.**

### 中文

**TBAO 保护人的意义主权，让 AI 在受控行动中成熟。**
