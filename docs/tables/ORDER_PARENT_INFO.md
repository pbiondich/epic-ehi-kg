# ORDER_PARENT_INFO

> This table will hold procedure order data where it is sometimes necessary to obtain the information from the parent (or possibly grandparent) order if it exists. Otherwise default to the child/Now order record's information in cases where there is no parent order.

**Primary key:** `ORDER_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier that consists of the order ID. Grandparent, parent and child orders will populate this table. |
| 2 | `PARENT_ORDER_ID` | NUMERIC |  | If the ID in the ORDER_ID column is a child order, then this column will hold the original order ID that instantiated the child (possibly a parent or possibly a grandparent order). If the ID in the ORDER_ID column is an order placed by an end user in the system (i.e. it was never instantiated- such as parent or grandparents), then this column will hold the same ID. |
| 3 | `ORDERING_DTTM` | DATETIME (Local) |  | This is the original ordering date and time of the order record in the PARENT_ORDER_ID column. For child orders, the date and time in ORDER_PROC.ORDER_INST is the date and time the order was released. |
| 4 | `ORD_LOGIN_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 5 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). This will be the contact used to place the order record in the PARENT_ORDER_ID column. For child orders, the contact serial number in ORDER_PROC.PAT_ENC_CSN_ID is the contact in which the order was released. |
| 6 | `PAT_CONTACT_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

