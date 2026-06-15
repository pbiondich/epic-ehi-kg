# DOCS_RCVD_INTRECIP

> The DOCS_RCVD_INTRECIP table contains information about the intended recipients to whom a given document from an external system was addressed.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `INTENDED_RECIP_NAME` | VARCHAR |  | When a submission set is received from an external system, it contains certain metadata supplied by the sending system regarding the document. This column contains the name of the intended recipient for a received message. |
| 5 | `INTENDED_RECIP_ADDR` | VARCHAR |  | When a submission set is received from an external system, it contains certain metadata supplied by the sending system regarding the document. This column contains the Direct address of an intended recipient for a received message. |
| 6 | `INTEND_RECIP_EMP_ID` | VARCHAR |  | Intended recipient employee ID column. When a submission set is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the employee ID for the intended recipient supplied in a received message, if one can be resolved. |
| 7 | `INTEND_RECIP_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `INTEND_RECIP_HIP_ID` | NUMERIC |  | Intended recipient In Basket Pool ID column. When a submission set is received from an external system, it will contain certain metadata supplied by the sending system regarding the document. This column contains the registry ID for the intended recipient supplied in a received message, if one can be resolved. |
| 9 | `INTEND_RECIP_HIP_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 10 | `RECPT_ACCESS_TYPE_C_NAME` | VARCHAR |  | This is a category value that indicates whether the intended recipient of a summary of care document is an EpicCare Link user, a Hyperspace user, or both. |
| 11 | `RECPT_PHY_ADDR` | VARCHAR |  | This item stores the physical address of the intended recipient. |
| 12 | `RECPT_PHONE` | VARCHAR |  | This item stores the phone number of the intended recipient. |
| 13 | `INTEND_RECIP_EAF_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 14 | `INTEND_RECIP_ROLE` | VARCHAR |  | Contains the name of the intended recipient's role for a received message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

