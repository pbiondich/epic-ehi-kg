# BLOOD_ADMIN_INFO

> This table holds the information for a blood unit associated with an order. The data includes the discrete information for the blood unit (including identifiers) as well as the scanning compliance for the discrete information.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BLOOD_ADMIN_UNIT` | VARCHAR |  | The unit number for the blood product documented as part of an administration. |
| 4 | `BLOOD_ADMIN_REG` | VARCHAR |  | The CODABAR Registration number for the blood product documented as part of an administration. |
| 5 | `BLOOD_ADMIN_PROD` | VARCHAR |  | The product code for the blood product documented as part of an administration. |
| 6 | `BLOOD_ADMIN_EXP_DTTM` | DATETIME (Local) |  | The expiration date for the blood product documented as part of an administration. |
| 7 | `BLOOD_ADMIN_TYPE` | VARCHAR |  | The blood type for the blood product documented as part of an administration. |
| 8 | `BLOOD_SCNCMP_UNIT_C_NAME` | VARCHAR |  | Indicates whether scanning of the blood unit field was compliant (11), not compliant (12), or not applicable (13) when the administration was documented. |
| 9 | `BLOOD_SCNCMP_REG_C_NAME` | VARCHAR |  | Indicates whether scanning of the blood registration number field was compliant (11), not compliant (12), or not applicable (13) when the administration was documented. |
| 10 | `BLOOD_SCNCMP_PC_C_NAME` | VARCHAR |  | Indicates whether scanning of the blood product code field was compliant (11), not compliant (12), or not applicable (13) when the administration was documented. |
| 11 | `BLOOD_SCNCMP_EXP_C_NAME` | VARCHAR |  | Indicates whether scanning of the blood expiration date field was compliant (11), not compliant (12), or not applicable (13) when the administration was documented. |
| 12 | `BLOOD_SCNCMP_TYPE_C_NAME` | VARCHAR |  | Indicates whether scanning of the blood type field was compliant (11), not compliant (12), or not applicable (13) when the administration was documented. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

