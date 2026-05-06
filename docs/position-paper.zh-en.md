# TBAO Position Paper v0.1 / TBAO 立场文档 v0.1

> Status / 状态: public draft / 公开草稿  
> Scope / 范围: conceptual and architectural positioning only / 仅限概念与架构定位

---

## 1. Position / 立场

### English

TBAO begins from a simple but hard design position:

> Human beings retain sovereignty over meaning. AI agents may reason broadly, but they may act only within bounded, reviewable, and recoverable authority.

As AI systems move from answering questions to using tools, writing memory, changing files, sending messages, modifying code, and connecting to external services, governance must move from rhetorical prompts into explicit runtime structure.

TBAO is an attempt to describe and implement that structure.

### 中文

TBAO 从一个简单但并不轻松的设计立场出发：

> 人拥有意义主权。AI Agent 可以广泛思考，但只能在有边界、可审查、可恢复的授权范围内行动。

当 AI 系统从回答问题走向调用工具、写入记忆、修改文件、发送消息、修改代码和连接外部服务时，治理不能停留在提示词修辞层面，必须进入明确的运行时结构。

TBAO 试图描述并实现这种结构。

---

## 2. The Risk / 风险

### English

The central risk is not only that AI may produce false answers. The more structural risk is that agentic systems may act on uncertain interpretation.

Typical failure modes include:

- treating inferred intent as confirmed intent;
- rewriting human preference through repeated suggestion;
- overwriting personal or organizational context with generic inference;
- turning temporary conversation into durable memory;
- escalating from advice into action without authority mapping;
- optimizing task completion while damaging the deeper human goal;
- leaving side effects that cannot be audited, reversed, or responsibly explained.

### 中文

核心风险不只是 AI 可能给出错误答案。更结构性的风险是：Agent 系统可能基于不确定解释采取行动。

典型失效模式包括：

- 把推断意图当成已确认意图；
- 通过反复建议重写人的偏好；
- 用通用推断覆盖个人或组织的具体上下文；
- 把临时对话固化为长期记忆；
- 在缺少授权映射的情况下从建议升级为行动；
- 为了完成任务而损害更深层的人类目标；
- 留下无法审计、无法恢复、无法负责任解释的副作用。

---

## 3. Design Claim / 设计主张

### English

Prompt-level safety is not enough for side-effectful agents.

A trustworthy agentic system needs at least three governance surfaces:

```text
Knowledge Governance -> Advisory Governance -> Action Governance
```

- Knowledge governance controls how human knowledge is used, confirmed, remembered, and reused.
- Advisory governance controls how judgment-shaping outputs are grounded, challenged, verified, and downgraded.
- Action governance controls how external-state-changing actions are requested, classified, decided, guarded, recorded, and recovered.

### 中文

对于有外部副作用的 Agent，提示词层面的安全是不够的。

一个可信的 Agent 系统至少需要三类治理界面：

```text
知识治理 -> 顾问治理 -> 行动治理
```

- 知识治理：约束人的知识如何被使用、确认、记忆和复用。
- 顾问治理：约束会影响人类判断的输出如何被溯源、质疑、校验和降级。
- 行动治理：约束改变外部状态的行动如何被请求、分级、裁决、守卫、记录和恢复。

---

## 4. First Proof Target / 第一证明目标

### English

TBAO v0.1 does not attempt to build a full Agent OS.

The first proof target is the **Action Spine MVP**:

```text
ActionRequest -> RiskClassifier -> PolicyDecision -> ExecutionGuard -> ActionLedger
```

This MVP should prove that an agent cannot directly jump from intent to side-effectful execution. It must first produce a structured action request, receive a risk tier, pass policy decision, meet execution guard controls, and leave a ledger entry for later review.

### 中文

TBAO v0.1 不尝试构建完整 Agent OS。

第一证明目标是 **Action Spine MVP / 行动脊柱 MVP**：

```text
行动请求 -> 风险分级 -> 策略裁决 -> 执行守卫 -> 行动账本
```

该 MVP 要证明：Agent 不能从意图直接跳到有副作用的执行。它必须先产生结构化行动请求，获得风险分级，通过策略裁决，满足执行守卫控制，并留下可复盘的行动账本。

---

## 5. Boundary / 边界

### English

This public draft is intentionally bounded.

It does not claim production readiness. It does not execute real high-risk actions. It does not replace legal, organizational, or human responsibility. It does not claim to solve all AI safety problems.

Its narrower claim is this:

> Side-effectful agent action should be structurally governed before it is executed.

### 中文

本公开草稿有意保持边界。

它不声称已经生产可用，不执行真实高风险动作，不替代法律、组织或人类责任，也不声称解决所有 AI 安全问题。

它更窄的主张是：

> 有外部副作用的 Agent 行动，在执行前必须被结构性治理。

---

## 6. North Star / 北极星

### English

Every future addition should pass this test:

```text
Does it protect human meaning sovereignty?
Does it preserve provenance, boundaries, and confirmation status?
Does it make judgment-shaping advice reviewable and downgradeable?
Does it make side-effectful action decidable, traceable, and recoverable?
```

### 中文

每一项未来新增内容都应通过这个测试：

```text
它是否保护人的意义主权？
它是否保留来源、边界和确认状态？
它是否让影响判断的建议可审查、可降级？
它是否让有外部副作用的行动可裁决、可追溯、可恢复？
```
