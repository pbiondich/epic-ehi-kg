# AP_CLAIM_IF_CODES

> This table contains the outgoing parameters and incoming edit codes, values, and descriptions for the claim and its services, for adjudications where the claim was submitted to an external PPS pricer via 837.

**Primary key:** `CLAIM_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK FK→ | The unique identifier for the claim info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ADJUDICATION_NUMBER` | INTEGER |  | Stores the adjudication number that the outgoing parameter or incoming response is associated with. This aligns with LINE for other tables in the interface related group tables (such as AP_CLAIM_IF_INFO*) and GROUP_LINE in the related-multi tables (such as AP_CLAIM_IF_OUT_OCC_CODE). |
| 4 | `TX_ID` | NUMERIC | shared | Stores the unique identifier of the service line (also known as an AP transaction), if the transaction is at the service-level. If the transaction is claim-level, this column will be NULL. |
| 5 | `CODE_NAME` | VARCHAR |  | The incoming response code received from the external pricer, or the outgoing parameter code sent to the external pricer. |
| 6 | `CODE_VALUE` | VARCHAR |  | The incoming response value from the external pricer, or the outgoing parameter value sent to the external pricer. |
| 7 | `CODE_DESCRIPTION` | VARCHAR |  | The description of the code and value. |
| 8 | `DIRECTION_C_NAME` | VARCHAR |  | Stores the category identifier that indicates if the code and value were an outgoing parameter to the external pricer, or an incoming code edit. This value can be translated using ZC_DIRECTION_2. |
| 9 | `SERVICE_LINE` | INTEGER |  | The service line that the incoming response or outgoing parameter code, value, and description are associated with. This row is not set for claim level responses from the interface. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CLAIM_ID` | [CLAIM_INFO](CLAIM_INFO.md) | overflow_master | medium |

