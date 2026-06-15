# DOCS_RCVD_ACTN_AUD

> This table stores the action audit performed on the discrete data.

**Primary key:** `DOCUMENT_ID`, `LINE`  
**Columns:** 21  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ACT_AUD_REF_ID` | VARCHAR |  | This item stores the reference identifier associated with the discrete data. |
| 4 | `ACT_AUD_ACT_TYPE_C_NAME` | VARCHAR |  | This item stores the type of action performed on the discrete data. |
| 5 | `ACT_AUD_ACT_USER_ID` | VARCHAR |  | This item stores the ID of the user performing the action on discrete data. |
| 6 | `ACT_AUD_ACT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `ACT_AUD_ACT_INST` | DATETIME (Local) |  | This item stores the instant of the audit action on the discrete data. |
| 8 | `ACT_AUD_ASSC_CSN` | NUMERIC |  | This item stores the associated contact where the discrete data resides. |
| 9 | `ACT_AUD_LPL_ID` | NUMERIC |  | This item stores the ID of the Problem List record if the discrete data was filed into the Problem List. |
| 10 | `ACT_AUD_ORD_ID` | NUMERIC |  | This item stores the ID of the Orders record if the discrete data was filed into an Order record. |
| 11 | `ACT_AUD_ACT_DESC` | VARCHAR |  | This item stores additional description about the action being taken. |
| 12 | `ACT_AUD_DATA_TYPE_C_NAME` | VARCHAR |  | This item stores the data type associated with the audit action. |
| 13 | `ACT_AUD_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 14 | `ACT_AUD_ERX_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 15 | `ACT_AUD_DC_RSN_C_NAME` | VARCHAR | org | This item stores the discontinue reason for the discontinue action made on an external medication. |
| 16 | `ACT_AUD_DC_RSN_FT` | VARCHAR |  | This item stores the free-text discontinue reason for the discontinue action made on an external medication. |
| 17 | `ACT_AUD_LOC_UPD_TYP_C_NAME` | VARCHAR |  | This item stores the type of action performed on local data using external data. |
| 18 | `ACT_AUD_INF_ID` | NUMERIC |  | This item stores the ID of the Infections record if the discrete data was filed into an Infections record. |
| 19 | `ACT_AUD_EDG_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 20 | `ACT_AUD_ORD_CONTACT_DATE` | NUMERIC |  | This item stores the DAT of the ORD record if the discrete data was filed into ORD. |
| 21 | `ACT_AUD_NOTE_ID` | VARCHAR |  | The unique ID of the a note which was auto-reconciled from a C-CDA document and was later deleted by the Auto-Reconciled Notes Cleanup Utliity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

