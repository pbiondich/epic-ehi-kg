# RYAN_WHITE_IMMNZTN

> This table contains immunization information from Ryan White abstractions.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RYN_WHT_IMMNZTN_IMMUNE_ID` | NUMERIC |  | An immunization record documented on the patient for Ryan White reporting. |
| 4 | `RYN_WHT_IMMNZTN_RECV_C_NAME` | VARCHAR |  | An immunization record's received code documented on the patient for Ryan White reporting. |
| 5 | `RYN_WHT_IMMNZTN_DATE` | DATETIME |  | An immunization record's date as documented on the patient for Ryan White reporting. |
| 6 | `RYN_WHT_IMMNZTN_IMMNTY_C_NAME` | VARCHAR |  | An immunization record's immunity code as documented on the patient for Ryan White reporting. |
| 7 | `RYN_WHT_IMMNZTN_IMMUN_ID` | NUMERIC |  | An immunization record documented on the patient for Ryan White reporting. |
| 8 | `RYN_WHT_IMMNZTN_IMMUN_ID_NAME` | VARCHAR |  | The name of the immunization. |
| 9 | `RYN_WHT_IMMNZTN_AMOUNT` | INTEGER |  | Amount of an immunization administered documented on the patient for Ryan White reporting. |
| 10 | `RYN_WHT_IMMNZTN_DISP_QTYUNIT_C_NAME` | VARCHAR | org | Unit of an immunization administered documented on the patient for Ryan White reporting. |
| 11 | `RYN_WHT_IMMNZTN_MFG_C_NAME` | VARCHAR | org | Manufacturer of an immunization administered documented on the patient for Ryan White reporting. |
| 12 | `RYN_WHT_IMMNZTN_MVX` | VARCHAR |  | Manufacturer code of an immunization administered documented on the patient for Ryan White reporting. |
| 13 | `RYN_WHT_IMMNZTN_LOT_NUMBER` | VARCHAR |  | Manufacturer code of an immunization administered documented on the patient for Ryan White reporting. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

