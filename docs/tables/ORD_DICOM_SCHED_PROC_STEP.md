# ORD_DICOM_SCHED_PROC_STEP

> This table contains information about orders' DICOM scheduled procedure step.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SPS_ID` | VARCHAR |  | The DICOM Scheduled Procedure Step ID. |
| 4 | `SPS_MOD_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 5 | `SPS_PROC_ID` | NUMERIC |  | The identifier (ID) of the procedure (OPE) record of the modality that this scheduled procedure step was generated for. |
| 6 | `SPS_APPT_PAT_ENC_CSN_ID` | NUMERIC | FK→ | The contact serial number of the appointment that this scheduled procedure step was generated for. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `SPS_APPT_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

