# CL_ORD_VALIDATION

> Order validation audit trail info like user/ instant/ work station /result/ dat etc.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 12  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ORDER_VAL_USR_ID` | VARCHAR |  | The unique identifier of the user who validated the order. |
| 4 | `ORDER_VAL_USR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ORD_VALID_INST` | DATETIME (Local) |  | The instant when the order record was validated. |
| 6 | `ORD_VALID_CONTEXT_NAME` | VARCHAR | org | list of special requirements a patient needs for transfused blood |
| 7 | `ORD_VALID_LWS_ID_WORKSTATION_NAME` | VARCHAR |  | This is the internal workstation name. |
| 8 | `ORD_VALIDAT_RES_C_NAME` | VARCHAR |  | The validation result category ID for the order. |
| 9 | `ORD_VALID_DAT` | INTEGER |  | The contact date (DAT) for when the order record was validated. |
| 10 | `ORDER_VAL_DEVICE_C_NAME` | VARCHAR | org | The device category ID for the order, indicating the type of device used for user authentication while validating this order. |
| 11 | `ORDER_VAL_NUM_FACT` | INTEGER |  | The number of factors used for user authentication while validating this order record. |
| 12 | `ORD_VALID_COMMENT` | VARCHAR |  | This is a technical comment for details about the specific event. This can contain technical information that is not immediately useful for end users and therefore should not be displayed within hyperspace or any other client. One use case is for non-live edit modifies to document why the order couldn't be live edit modified. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

