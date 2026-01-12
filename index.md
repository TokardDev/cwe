# Security Requirements - CWE Index (Hardware Design View 1194)

This document indexes all Common Weakness Enumeration (CWE) entries for Hardware Design.

---

## 1195 - Manufacturing and Life Cycle Management Concerns

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-1059](1195-manufacturing-lifecycle/cwe-1059.md) | Insufficient Technical Documentation | Done |
| [CWE-1248](1195-manufacturing-lifecycle/cwe-1248.md) | Semiconductor Defects in Hardware Logic with Security-Sensitive Implications | Done |
| [CWE-1266](1195-manufacturing-lifecycle/cwe-1266.md) | Improper Scrubbing of Sensitive Data from Decommissioned Device | Done |
| [CWE-1269](1195-manufacturing-lifecycle/cwe-1269.md) | Product Released in Non-Release Configuration | Done |
| [CWE-1273](1195-manufacturing-lifecycle/cwe-1273.md) | Device Unlock Credential Sharing | Done |
| [CWE-1297](1195-manufacturing-lifecycle/cwe-1297.md) | Unprotected Confidential Information on Device is Accessible by OSAT Vendors | Done |

---

## 1196 - Security Flow Issues

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-1190](1196-security-flow/cwe-1190.md) | DMA Device Enabled Too Early in Boot Phase | Done |
| [CWE-1193](1196-security-flow/cwe-1193.md) | Power-On of Untrusted Execution Core Before Enabling Fabric Access Control | Done |
| [CWE-1264](1196-security-flow/cwe-1264.md) | Hardware Logic with Insecure De-Synchronization between Control and Data Channels | Done |
| [CWE-1274](1196-security-flow/cwe-1274.md) | Improper Access Control for Volatile Memory Containing Boot Code | Done |
| [CWE-1283](1196-security-flow/cwe-1283.md) | Mutable Attestation or Measurement Reporting Data | Done |
| [CWE-1310](1196-security-flow/cwe-1310.md) | Missing Ability to Patch ROM Code | Done |
| [CWE-1326](1196-security-flow/cwe-1326.md) | Missing Immutable Root of Trust in Hardware | Done |
| [CWE-1328](1196-security-flow/cwe-1328.md) | Security Version Number Mutable to Older Versions | Done |

---

## 1197 - Integration Issues

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-1276](1197-integration/cwe-1276.md) | Hardware Child Block Incorrectly Connected to Parent System | Done |

---

## 1198 - Privilege Separation and Access Control Issues

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-276](1198-privilege-access-control/cwe-276.md) | Incorrect Default Permissions | Done |
| [CWE-441](1198-privilege-access-control/cwe-441.md) | Unintended Proxy or Intermediary ('Confused Deputy') | Done |
| [CWE-1189](1198-privilege-access-control/cwe-1189.md) | Improper Isolation of Shared Resources on System-on-a-Chip (SoC) | Done |
| [CWE-1192](1198-privilege-access-control/cwe-1192.md) | Improper Identifier for IP Block used in System-On-Chip (SOC) | Done |
| [CWE-1220](1198-privilege-access-control/cwe-1220.md) | Insufficient Granularity of Access Control | Done |
| [CWE-1222](1198-privilege-access-control/cwe-1222.md) | Insufficient Granularity of Address Regions Protected by Register Locks | Done |
| [CWE-1242](1198-privilege-access-control/cwe-1242.md) | Inclusion of Undocumented Features or Chicken Bits | Done |
| [CWE-1259](1198-privilege-access-control/cwe-1259.md) | Improper Restriction of Security Token Assignment | Done |
| [CWE-1260](1198-privilege-access-control/cwe-1260.md) | Improper Handling of Overlap Between Protected Memory Ranges | Done |
| [CWE-1262](1198-privilege-access-control/cwe-1262.md) | Improper Access Control for Register Interface | Done |
| [CWE-1267](1198-privilege-access-control/cwe-1267.md) | Policy Uses Obsolete Encoding | Done |
| [CWE-1268](1198-privilege-access-control/cwe-1268.md) | Policy Privileges are not Assigned Consistently Between Control and Data Agents | Done |
| [CWE-1270](1198-privilege-access-control/cwe-1270.md) | Generation of Incorrect Security Tokens | Done |
| [CWE-1280](1198-privilege-access-control/cwe-1280.md) | Access Control Check Implemented After Asset is Accessed | Done |
| [CWE-1290](1198-privilege-access-control/cwe-1290.md) | Incorrect Decoding of Security Identifiers | Done |
| [CWE-1292](1198-privilege-access-control/cwe-1292.md) | Incorrect Conversion of Security Identifiers | Done |
| [CWE-1294](1198-privilege-access-control/cwe-1294.md) | Insecure Security Identifier Mechanism | Done |
| [CWE-1299](1198-privilege-access-control/cwe-1299.md) | Missing Protection Mechanism for Alternate Hardware Interface | Done |
| [CWE-1302](1198-privilege-access-control/cwe-1302.md) | Missing Source Identifier in Entity Transactions on a System-On-Chip (SOC) | Done |
| [CWE-1303](1198-privilege-access-control/cwe-1303.md) | Non-Transparent Sharing of Microarchitectural Resources | Done |
| [CWE-1314](1198-privilege-access-control/cwe-1314.md) | Missing Write Protection for Parametric Data Values | Done |
| [CWE-1318](1198-privilege-access-control/cwe-1318.md) | Missing Support for Security Features in On-chip Fabrics or Buses | Done |
| [CWE-1334](1198-privilege-access-control/cwe-1334.md) | Unauthorized Error Injection Can Degrade Hardware Redundancy | Done |
| [CWE-1420](1198-privilege-access-control/cwe-1420.md) | Exposure of Sensitive Information during Transient Execution | Done (↗1201) |
| [CWE-1421](1198-privilege-access-control/cwe-1421.md) | Exposure of Sensitive Information in Shared Microarchitectural Structures during Transient Execution | Done (↗1201) |
| [CWE-1422](1198-privilege-access-control/cwe-1422.md) | Exposure of Sensitive Information caused by Incorrect Data Forwarding during Transient Execution | Done (↗1201) |
| [CWE-1423](1198-privilege-access-control/cwe-1423.md) | Exposure of Sensitive Information caused by Shared Microarchitectural Predictor State that Influences Transient Execution | Done (↗1201) |

---

## 1199 - General Circuit and Logic Design Concerns

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-1209](1199-circuit-logic-design/cwe-1209.md) | Failure to Disable Reserved Bits | Done |
| [CWE-1221](1199-circuit-logic-design/cwe-1221.md) | Incorrect Register Defaults or Module Parameters | Done |
| [CWE-1223](1199-circuit-logic-design/cwe-1223.md) | Race Condition for Write-Once Attributes | Done |
| [CWE-1224](1199-circuit-logic-design/cwe-1224.md) | Improper Restriction of Write-Once Bit Fields | Done |
| [CWE-1231](1199-circuit-logic-design/cwe-1231.md) | Improper Prevention of Lock Bit Modification | Done |
| [CWE-1232](1199-circuit-logic-design/cwe-1232.md) | Improper Lock Behavior After Power State Transition | Done |
| [CWE-1233](1199-circuit-logic-design/cwe-1233.md) | Security-Sensitive Hardware Controls with Missing Lock Bit Protection | Done |
| [CWE-1234](1199-circuit-logic-design/cwe-1234.md) | Hardware Internal or Debug Modes Allow Override of Locks | Done |
| [CWE-1245](1199-circuit-logic-design/cwe-1245.md) | Improper Finite State Machines (FSMs) in Hardware Logic | Done |
| [CWE-1250](1199-circuit-logic-design/cwe-1250.md) | Improper Preservation of Consistency Between Independent Representations of Shared State | Done |
| [CWE-1253](1199-circuit-logic-design/cwe-1253.md) | Incorrect Selection of Fuse Values | Done |
| [CWE-1254](1199-circuit-logic-design/cwe-1254.md) | Incorrect Comparison Logic Granularity | Done |
| [CWE-1261](1199-circuit-logic-design/cwe-1261.md) | Improper Handling of Single Event Upsets | Done |
| [CWE-1298](1199-circuit-logic-design/cwe-1298.md) | Hardware Logic Contains Race Conditions | Done |

---

## 1201 - Core and Compute Issues

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-1252](1201-core-compute/cwe-1252.md) | CPU Hardware Not Configured to Support Exclusivity of Write and Execute Operations | Done |
| [CWE-1281](1201-core-compute/cwe-1281.md) | Sequence of Processor Instructions Leads to Unexpected Behavior | Done |
| [CWE-1342](1201-core-compute/cwe-1342.md) | Information Exposure through Microarchitectural State after Transient Execution | Done |
| [CWE-1420](1201-core-compute/cwe-1420.md) | Exposure of Sensitive Information during Transient Execution | Done |
| [CWE-1421](1201-core-compute/cwe-1421.md) | Exposure of Sensitive Information in Shared Microarchitectural Structures during Transient Execution | Done |
| [CWE-1422](1201-core-compute/cwe-1422.md) | Exposure of Sensitive Information caused by Incorrect Data Forwarding during Transient Execution | Done |
| [CWE-1423](1201-core-compute/cwe-1423.md) | Exposure of Sensitive Information caused by Shared Microarchitectural Predictor State that Influences Transient Execution | Done |

---

## 1202 - Memory and Storage Issues

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-226](1202-memory-storage/cwe-226.md) | Sensitive Information in Resource Not Removed Before Reuse | Done |
| [CWE-1239](1202-memory-storage/cwe-1239.md) | Improper Zeroization of Hardware Register | Done |
| [CWE-1246](1202-memory-storage/cwe-1246.md) | Improper Write Handling in Limited-write Non-Volatile Memories | Done |
| [CWE-1251](1202-memory-storage/cwe-1251.md) | Mirrored Regions with Different Values | Done |
| [CWE-1257](1202-memory-storage/cwe-1257.md) | Improper Access Control Applied to Mirrored or Aliased Memory Regions | Done |
| [CWE-1282](1202-memory-storage/cwe-1282.md) | Assumed-Immutable Data is Stored in Writable Memory | Done |
| [CWE-1342](1202-memory-storage/cwe-1342.md) | Information Exposure through Microarchitectural State after Transient Execution | Done (↗1201) |
| [CWE-1420](1202-memory-storage/cwe-1420.md) | Exposure of Sensitive Information during Transient Execution | Done (↗1201) |
| [CWE-1421](1202-memory-storage/cwe-1421.md) | Exposure of Sensitive Information in Shared Microarchitectural Structures during Transient Execution | Done (↗1201) |
| [CWE-1422](1202-memory-storage/cwe-1422.md) | Exposure of Sensitive Information caused by Incorrect Data Forwarding during Transient Execution | Done (↗1201) |
| [CWE-1423](1202-memory-storage/cwe-1423.md) | Exposure of Sensitive Information caused by Shared Microarchitectural Predictor State that Influences Transient Execution | Done (↗1201) |

---

## 1203 - Peripherals, On-chip Fabric, and Interface/IO Problems

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-1311](1203-peripherals-fabric-io/cwe-1311.md) | Improper Translation of Security Attributes by Fabric Bridge | Done |
| [CWE-1312](1203-peripherals-fabric-io/cwe-1312.md) | Missing Protection for Mirrored Regions in On-Chip Fabric Firewall | Done |
| [CWE-1315](1203-peripherals-fabric-io/cwe-1315.md) | Improper Setting of Bus Controlling Capability in Fabric End-point | Done |
| [CWE-1316](1203-peripherals-fabric-io/cwe-1316.md) | Fabric-Address Map Allows Programming of Unwarranted Overlaps of Protected and Unprotected Ranges | Done |
| [CWE-1317](1203-peripherals-fabric-io/cwe-1317.md) | Improper Access Control in Fabric Bridge | Done |
| [CWE-1331](1203-peripherals-fabric-io/cwe-1331.md) | Improper Isolation of Shared Resources in Network On Chip (NoC) | Done |

---

## 1205 - Security Primitives and Cryptography Issues

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-203](1205-security-primitives-crypto/cwe-203.md) | Observable Discrepancy | Done |
| [CWE-325](1205-security-primitives-crypto/cwe-325.md) | Missing Cryptographic Step | Done |
| [CWE-1240](1205-security-primitives-crypto/cwe-1240.md) | Use of a Cryptographic Primitive with a Risky Implementation | Done |
| [CWE-1241](1205-security-primitives-crypto/cwe-1241.md) | Use of Predictable Algorithm in Random Number Generator | Done |
| [CWE-1279](1205-security-primitives-crypto/cwe-1279.md) | Cryptographic Operations are run Before Supporting Units are Ready | Done |
| [CWE-1300](1205-security-primitives-crypto/cwe-1300.md) | Improper Protection of Physical Side Channels | Done |
| [CWE-1351](1205-security-primitives-crypto/cwe-1351.md) | Improper Handling of Hardware Behavior in Exceptionally Cold Environments | Done |
| [CWE-1431](1205-security-primitives-crypto/cwe-1431.md) | Driving Intermediate Cryptographic State/Results to Hardware Module Outputs | Done |

---

## 1206 - Power, Clock, Thermal, and Reset Concerns

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-1232](1206-power-clock-thermal-reset/cwe-1232.md) | Improper Lock Behavior After Power State Transition | Done (↗1199) |
| [CWE-1247](1206-power-clock-thermal-reset/cwe-1247.md) | Improper Protection Against Voltage and Clock Glitches | Done |
| [CWE-1248](1206-power-clock-thermal-reset/cwe-1248.md) | Semiconductor Defects in Hardware Logic with Security-Sensitive Implications | Done (↗1195) |
| [CWE-1255](1206-power-clock-thermal-reset/cwe-1255.md) | Comparison Logic is Vulnerable to Power Side-Channel Attacks | Done |
| [CWE-1256](1206-power-clock-thermal-reset/cwe-1256.md) | Improper Restriction of Software Interfaces to Hardware Features | Done |
| [CWE-1271](1206-power-clock-thermal-reset/cwe-1271.md) | Uninitialized Value on Reset for Registers Holding Security Settings | Done |
| [CWE-1304](1206-power-clock-thermal-reset/cwe-1304.md) | Improperly Preserved Integrity of Hardware Configuration State During a Power Save/Restore Operation | Done |
| [CWE-1314](1206-power-clock-thermal-reset/cwe-1314.md) | Missing Write Protection for Parametric Data Values | Done (↗1198) |
| [CWE-1320](1206-power-clock-thermal-reset/cwe-1320.md) | Improper Protection for Outbound Error Messages and Alert Signals | Done |
| [CWE-1332](1206-power-clock-thermal-reset/cwe-1332.md) | Improper Handling of Faults that Lead to Instruction Skips | Done |
| [CWE-1338](1206-power-clock-thermal-reset/cwe-1338.md) | Improper Protections Against Hardware Overheating | Done |

---

## 1207 - Debug and Test Problems

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-319](1207-debug-test/cwe-319.md) | Cleartext Transmission of Sensitive Information | Done |
| [CWE-1191](1207-debug-test/cwe-1191.md) | On-Chip Debug and Test Interface With Improper Access Control | Done |
| [CWE-1234](1207-debug-test/cwe-1234.md) | Hardware Internal or Debug Modes Allow Override of Locks | Done (↗1199) |
| [CWE-1243](1207-debug-test/cwe-1243.md) | Sensitive Non-Volatile Information Not Protected During Debug | Done |
| [CWE-1244](1207-debug-test/cwe-1244.md) | Internal Asset Exposed to Unsafe Debug Access Level or State | Done |
| [CWE-1258](1207-debug-test/cwe-1258.md) | Exposure of Sensitive System Information Due to Uncleared Debug Information | Done |
| [CWE-1272](1207-debug-test/cwe-1272.md) | Sensitive Information Uncleared Before Debug/Power State Transition | Done |
| [CWE-1291](1207-debug-test/cwe-1291.md) | Public Key Re-Use for Signing both Debug and Production Code | Done |
| [CWE-1295](1207-debug-test/cwe-1295.md) | Debug Messages Revealing Unnecessary Information | Done |
| [CWE-1296](1207-debug-test/cwe-1296.md) | Incorrect Chaining or Granularity of Debug Components | Done |
| [CWE-1313](1207-debug-test/cwe-1313.md) | Hardware Allows Activation of Test or Debug Logic at Runtime | Done |
| [CWE-1323](1207-debug-test/cwe-1323.md) | Improper Management of Sensitive Trace Data | Done |

---

## 1208 - Cross-Cutting Problems

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-440](1208-cross-cutting/cwe-440.md) | Expected Behavior Violation | Done |
| [CWE-1053](1208-cross-cutting/cwe-1053.md) | Missing Documentation for Design | Done |
| [CWE-1059](1208-cross-cutting/cwe-1059.md) | Insufficient Technical Documentation | Done (↗1195) |
| [CWE-1263](1208-cross-cutting/cwe-1263.md) | Improper Physical Access Control | Done |
| [CWE-1277](1208-cross-cutting/cwe-1277.md) | Firmware Not Updateable | Done |
| [CWE-1301](1208-cross-cutting/cwe-1301.md) | Insufficient or Incomplete Data Removal within Hardware Component | Done |
| [CWE-1329](1208-cross-cutting/cwe-1329.md) | Reliance on Component That is Not Updateable | Done |
| [CWE-1330](1208-cross-cutting/cwe-1330.md) | Remanent Data Readable after Memory Erase | Done |
| [CWE-1357](1208-cross-cutting/cwe-1357.md) | Reliance on Insufficiently Trustworthy Component | Done |
| [CWE-1429](1208-cross-cutting/cwe-1429.md) | Missing Security-Relevant Feedback for Unexecuted Operations in Hardware Interface | Done |

---

## 1388 - Physical Access Issues and Concerns

| CWE ID | Title | Status |
|--------|-------|--------|
| [CWE-1247](1388-physical-access/cwe-1247.md) | Improper Protection Against Voltage and Clock Glitches | Done (↗1206) |
| [CWE-1248](1388-physical-access/cwe-1248.md) | Semiconductor Defects in Hardware Logic with Security-Sensitive Implications | Done (↗1195) |
| [CWE-1255](1388-physical-access/cwe-1255.md) | Comparison Logic is Vulnerable to Power Side-Channel Attacks | Done (↗1206) |
| [CWE-1261](1388-physical-access/cwe-1261.md) | Improper Handling of Single Event Upsets | Done (↗1199) |
| [CWE-1278](1388-physical-access/cwe-1278.md) | Missing Protection Against Hardware Reverse Engineering Using Integrated Circuit (IC) Imaging Techniques | Done |
| [CWE-1300](1388-physical-access/cwe-1300.md) | Improper Protection of Physical Side Channels | Done (↗1205) |
| [CWE-1319](1388-physical-access/cwe-1319.md) | Improper Protection against Electromagnetic Fault Injection (EM-FI) | Done |
| [CWE-1332](1388-physical-access/cwe-1332.md) | Improper Handling of Faults that Lead to Instruction Skips | Done (↗1206) |
| [CWE-1351](1388-physical-access/cwe-1351.md) | Improper Handling of Hardware Behavior in Exceptionally Cold Environments | Done (↗1205) |
| [CWE-1384](1388-physical-access/cwe-1384.md) | Improper Handling of Physical or Environmental Conditions | Done |
