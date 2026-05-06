# Action Spine MVP Example / 行动脊柱 MVP 示例

> Status / 状态: placeholder for v0.1 mock-only example / v0.1 模拟示例占位  
> Boundary / 边界: no real execution / 不真实执行

---

## English

This directory will contain the first runnable Action Spine MVP example.

The first example must remain:

```text
local-only
mock-only
non-executing
no real credentials
no real filesystem mutation
no real network mutation
no production access
```

The expected demo flow:

```text
1. receive a sample user intent;
2. convert it into ActionRequest;
3. classify the risk tier;
4. generate PolicyDecision;
5. simulate ExecutionGuard;
6. write a mock ActionLedger entry;
7. print the full decision trace.
```

The example should prove that TBAO can force side-effectful action through a structured governance path before execution.

---

## 中文

本目录将放置第一版可运行的 Action Spine MVP 示例。

第一版示例必须保持：

```text
仅本地
仅模拟
不真实执行
不使用真实密钥
不真实修改文件系统
不真实修改网络状态
不访问生产环境
```

预期演示流程：

```text
1. 接收一个示例用户意图；
2. 转换为 ActionRequest；
3. 完成风险分级；
4. 生成 PolicyDecision；
5. 模拟 ExecutionGuard；
6. 写入模拟 ActionLedger；
7. 打印完整裁决链路。
```

该示例要证明：TBAO 可以强制有外部副作用的行动，在执行前进入结构化治理路径。

---

## Initial Example Cases / 初始示例用例

```text
safe_thought          -> L0 -> ALLOW
read_only_scan        -> L1 -> ALLOW_LOG
mock_file_write       -> L2 -> ALLOW_MOCK_ONLY
durable_memory_write  -> L3 -> REQUIRE_APPROVAL
file_delete           -> L4 -> DENY_BY_DEFAULT
external_message_send -> L4 -> DENY_BY_DEFAULT
```

No real execution should be added before the safety boundary is reviewed.

在安全边界被审查前，不应添加真实执行能力。
