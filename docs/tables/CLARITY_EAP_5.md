# CLARITY_EAP_5

> The CLARITY_EAP_5 table contains basic information about the procedure records in your system. This includes both A/R and clinical procedures. This is a continuation of Clarity table CLARITY_EAP.

**Overflow of:** [CLARITY_EAP](CLARITY_EAP.md)  
**Primary key:** `PROC_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROC_ID` | NUMERIC | PK | The unique identifier (.1 item) for the procedure record. |
| 2 | `MYC_TKT_OVR_RULE_ID` | VARCHAR |  | Specify a rule to determine when to allow manually sending appointment requests to the patient for scheduling. |
| 3 | `MYC_TKT_OVR_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [CLARITY_EAP](CLARITY_EAP.md).

