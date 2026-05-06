# Action Spine MVP / 行动脊柱 MVP

> Status / 状态: v0.1 public draft / v0.1 公开草稿  
> Boundary / 边界: local-only, mock-only, non-executing / 仅本地、仅模拟、不真实执行

---

## 1. Purpose / 目的

### English

The Action Spine MVP is the first implementable cut of TBAO.

It proves one thing:

> An AI agent should not jump directly from intent to side-effectful execution.

Before execution, the agent must produce a structured action request, receive a risk tier, pass policy decision, satisfy execution guard controls, and leave an action ledger record.

### 中文

Action Spine MVP 是 TBAO 的第一版可实施切口。

它只证明一件事：

> AI Agent 不应从意图直接跳到有外部副作用的执行。

在执行前，Agent 必须先产生结构化行动请求，获得风险分级，通过策略裁决，满足执行守卫控制，并留下行动账本记录。

---

## 2. Minimal Flow / 最小流程

```text
Intent
  -> ActionRequest
  -> RiskClassifier
  -> PolicyDecision
  -> ExecutionGuard
  -> ActionLedger
```

中文：

```text
意图
  -> 行动请求
  -> 风险分级
  -> 策略裁决
  -> 执行守卫
  -> 行动账本
```

---

## 3. Risk Tier Model / 风险分级模型

```text
L0: pure thought, analysis, draft, simulation
L1: read-only inspection, tests, scans
L2: low-risk writes, temporary files, draft files
L3: configuration changes, dependency install, code commit, durable memory write
L4: deletion, payment, trade, external message send, production modification, credential access
```

```text
L0：纯思考、分析、草稿、方案推演
L1：只读检查、测试、扫描
L2：低风险写入、临时文件、草稿文件
L3：配置修改、依赖安装、代码提交、长期记忆写入
L4：删除、支付、交易、外部消息发送、生产环境修改、密钥访问
```

Default handling:

```text
L0: allow freely
L1: allow + log
L2: allow + log + rollback note
L3: require policy allowlist or human approval
L4: deny by default or require strong human approval
```

默认处理：

```text
L0：自由允许
L1：允许 + 记录
L2：允许 + 记录 + 回滚说明
L3：需要策略白名单或人工确认
L4：默认拒绝或强人工审批
```

---

## 4. Core Objects / 核心对象

### ActionRequest / 行动请求

```json
{
  "action_id": "act_demo_001",
  "actor": "agent.main",
  "requested_by": "human.owner",
  "action_type": "file.write",
  "target": "mock:/workspace/draft.md",
  "intent": "create a draft document",
  "evidence": ["user requested a draft document"],
  "side_effect": "low",
  "environment": "local_mock",
  "timestamp": "2026-05-06T00:00:00Z"
}
```

### PolicyDecision / 策略裁决

```json
{
  "action_id": "act_demo_001",
  "decision": "ALLOW_MOCK_ONLY",
  "risk_tier": "L2",
  "reason": "low-risk mock file write; no real filesystem mutation allowed in v0.1",
  "required_controls": ["mock_only", "log_action", "rollback_note"],
  "human_approval_required": false
}
```

### ActionLedger / 行动账本

```json
{
  "action_id": "act_demo_001",
  "decision": "ALLOW_MOCK_ONLY",
  "executed": false,
  "mock_executed": true,
  "result": "simulated file write",
  "rollback_available": "not applicable; no real mutation",
  "incident_status": "none"
}
```

---

## 5. MVP Safety Boundary / MVP 安全边界

The v0.1 MVP must remain:

```text
local-only
mock-only
non-executing
no real credentials
no real network mutation
no real file deletion
no real financial action
no real medical or legal action
no production environment access
```

v0.1 MVP 必须保持：

```text
仅本地
仅模拟
不真实执行
不使用真实密钥
不产生真实网络修改
不执行真实文件删除
不执行真实金融动作
不执行真实医疗或法律动作
不访问生产环境
```

---

## 6. Priority Action Types / 优先行动类型

Future examples may classify these action types, but v0.1 should simulate rather than execute them:

```text
shell.command
file.write
file.delete
memory.write
message.send
git.commit
git.push
http.request
plugin.install
config.modify
```

未来示例可以对以下行动类型分级，但 v0.1 应模拟而不真实执行：

```text
shell.command
file.write
file.delete
memory.write
message.send
git.commit
git.push
http.request
plugin.install
config.modify
```

---

## 7. Six-Question Test / 六问测试

Every medium-risk or high-risk side-effectful action should answer these questions before execution:

```text
1. What human meaning or goal is this action serving?
2. What evidence supports that interpretation?
3. Who has authority to approve or reject the action?
4. What risk tier applies?
5. What will be recorded for audit and recovery?
6. How can the action be stopped, rolled back, quarantined, or reviewed?
```

每一个中高风险有外部副作用的行动，在执行前都应回答：

```text
1. 这个行动服务于什么人类意义或目标？
2. 支持该解释的证据是什么？
3. 谁有权批准或拒绝该行动？
4. 适用什么风险等级？
5. 审计和恢复将记录什么？
6. 如何停止、回滚、隔离或复盘该行动？
```

---

## 8. v0.1 Success Criteria / v0.1 成功标准

The first MVP is successful if it can demonstrate:

```text
1. intent is converted into structured ActionRequest;
2. action type is classified into a risk tier;
3. policy decision is explicit;
4. real execution is blocked by default;
5. mock execution is logged;
6. reviewer can reconstruct the decision path.
```

第一版 MVP 如果能演示以下内容，即视为成功：

```text
1. 意图被转换为结构化 ActionRequest；
2. 行动类型被分级为风险等级；
3. 策略裁决是明确的；
4. 真实执行默认被阻断；
5. 模拟执行被记录；
6. 审查者可以重建裁决路径。
```
