# MAR_ADDL_INFO

> Table for contact level additional information such as barcode scans.

**Primary key:** `ORDER_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 16  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `SCANNED_BARCODE` | VARCHAR |  | The raw data captured during barcode scanning. |
| 5 | `NDC_CSN_ID` | VARCHAR |  | The CSN of the corresponding NDC. This can come from either scanning an NDC or entering one in the additional information grid for an administration. |
| 6 | `ORD_ID` | NUMERIC |  | When an ORD ID barcode is scanned, this is the order ID. |
| 7 | `SCANNED_DOSE` | VARCHAR |  | The scanned dose from the barcode if it is available. |
| 8 | `SCANNED_DOSE_UNIT_C_NAME` | VARCHAR | org | The scanned dose unit category number from the barcode for the administration, if it is available. |
| 9 | `LOT_NUM` | VARCHAR |  | The associated lot number with this medication administration. This can come from either barcode scanning or entering the lot number in the additional information grid. |
| 10 | `EXP_DATE` | DATETIME |  | The associated expiration date with this medication administration. This can come from either barcode scanning or entering the expiration date in the additional information grid. |
| 11 | `MED_BILL_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 12 | `SCANNED_CONCNTRTN` | VARCHAR |  | The concentration from a barcode scan or entered as part of additional info. |
| 13 | `MED_BILL_UCL_ID` | VARCHAR |  | The unique ID of the charge dropped for this NDC. |
| 14 | `SCANNED_CONC_UNIT_C_NAME` | VARCHAR |  | The concentration unit from a barcode scan or entered as part of additional info. |
| 15 | `COMPOUNDING_CNR_ID_RECORD_NAME` | VARCHAR |  | The name of the Compounding and Repackaging record. Compounding and repackaging records represent the products created when pharmacists combine multiple medications to create a new medication or take one medication from a container and place it into another container. |
| 16 | `PSP_IDENT` | VARCHAR |  | The identifier associated with the Patient-Specific Package barcode scan. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

