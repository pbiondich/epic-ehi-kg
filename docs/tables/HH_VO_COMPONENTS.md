# HH_VO_COMPONENTS

> This table contains Home Health verbal orders components information. This information is used to track changes made to verbal orders on the Home Health Remote Client.

**Primary key:** `VERBAL_ORDER_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `VERBAL_ORDER_ID` | VARCHAR | PK FK→ | The unique identifier for the verbal order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMPON_TYPE_C_NAME` | VARCHAR | org | Verbal orders component type. Links to category table ZC_COMP_TYPE. |
| 4 | `COMPON_OLD_MED_ID` | NUMERIC |  | Old medication verbal order ID. Links to table ORDER_PROC. |
| 5 | `COMPON_NEW_MED_ID` | VARCHAR |  | New medication verbal order ID. |
| 6 | `COMPON_VST_DISC_C_NAME` | VARCHAR | org | Verbal order component visit discipline. Links to category table ZC_COMPON_VST_DISC. |
| 7 | `COMPON_NOTES_ID` | VARCHAR |  | Verbal order component note ID. |
| 8 | `COMPON_CERT_PER` | VARCHAR |  | Verbal order component certification period. |
| 9 | `COMPON_EPS_CARE_ID` | NUMERIC |  | Verbal order component episode of care ID. Links to EPISODE table. |
| 10 | `COMPON_LINK_COMP` | VARCHAR |  | Verbal order component linked component. This item is used to store the link to the components for which this verbal order component is created. |
| 11 | `COMP_PENDING_FAX_YN` | VARCHAR |  | This item stores whether the verbal order component has been pended. |
| 12 | `COMPON_TAKING_DIFF_LINE` | INTEGER |  | This item stores the pointer to the patient taking differently line associated with a Home Health medication verbal order, if it exists. |
| 13 | `DISCON_MED_TEXT` | VARCHAR |  | Additional information on why an order's medication is discontinued. |
| 14 | `MED_AUDIT_LINE` | INTEGER |  | The line number for the medication audit trail. This is the line number found in column LINE of AUDIT_ORD_RXNOADD. |
| 15 | `SUPPL_ORDER_NOT_SENT_ALL_YN` | VARCHAR |  | Whether the order has been sent to all the providers who should be notified of changes to the plan of care. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `VERBAL_ORDER_ID` | [HH_VO_INFO](HH_VO_INFO.md) | sole_pk | high |

