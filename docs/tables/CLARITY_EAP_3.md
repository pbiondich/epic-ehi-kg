# CLARITY_EAP_3

> The CLARITY_EAP_3 table contains basic information about the procedure records in your system. This includes both A/R and clinical procedures. This is a continuation of Clarity table CLARITY_EAP.

**Overflow of:** [CLARITY_EAP](CLARITY_EAP.md)  
**Primary key:** `PROC_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 2 | `PT_FRIENDLY_NAME` | VARCHAR |  | The patient friendly procedure name for use in MyChart. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [CLARITY_EAP](CLARITY_EAP.md).

