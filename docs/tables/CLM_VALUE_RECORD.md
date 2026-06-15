# CLM_VALUE_RECORD

> This table holds basic identification and processing information for the claim value record.

**Primary key:** `RECORD_ID`  
**Columns:** 13  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim values record. |
| 2 | `RECORD_CREATION_DT` | DATETIME |  | The date the record was created. |
| 3 | `CLM_TYP_C_NAME` | VARCHAR | org | The type of claim values stored in the record. CMS is used for professional and dental claims. UB is used for institutional claims. |
| 4 | `FORM_TYP_C_NAME` | VARCHAR |  | The type of form used during processing. |
| 5 | `CONTEXT_C_NAME` | VARCHAR |  | The direction of the claim file, either incoming or outgoing. This value is only set for Accounts Payable claims. |
| 6 | `AP_CLAIM_ID` | NUMERIC |  | The claim information record associated with the invoice. This value is only set for Accounts Payable claims. |
| 7 | `SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 8 | `HEALTH_SYS_IDENT` | VARCHAR |  | This item holds the Health System Identifier (HSI) of the source for the claim. |
| 9 | `SOURCE_ORGANIZATION_ID` | NUMERIC |  | The source organization of the external record. This value is only set for external claims. |
| 10 | `SOURCE_ORGANIZATION_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 11 | `CLAIM_RECON_ID` | VARCHAR |  | The claim reconciliation record ID (CRD) associated with the claim data. |
| 12 | `CRD_CONTACT_DATE_REAL` | NUMERIC |  | The contact date of the claim reconciliation record, in internal format. |
| 13 | `CLAIM_OUTCOME_C_NAME` | VARCHAR |  | The outcome of the claim on its way to being paid. Complete: the claim is paid, Error: the claim will not be paid, Partial: the claim is current in the system but not paid yet, Queued: the claim is new. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

