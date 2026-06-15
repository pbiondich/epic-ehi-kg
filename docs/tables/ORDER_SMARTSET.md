# ORDER_SMARTSET

> This table contains data on smartsets and smartgroups that orders originated from.

**Primary key:** `ORDER_ID`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | Unique ID of the order record being retrieved |
| 2 | `SS_PRL_ID` | NUMERIC |  | The ID of the SmartSet or Order Set the order came from. |
| 3 | `SS_PRL_ID_PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| 4 | `SS_DAT` | VARCHAR |  | The contact date of the contact in the SmartSet that the order came from. |
| 5 | `SS_SG_KEY` | VARCHAR |  | The unique key assigned to the merged SmartGroup that contained this order. This is an arbitrary string value. |
| 6 | `MERGE_TMPL_ID` | NUMERIC |  | The ID of the merge template used when merging this SmartSet during ordering, if any. |
| 7 | `MERGE_TMPL_ID_PROTOCOL_NAME` | VARCHAR |  | The SmartSet/Protocol record name. This is different from the display name, which is stored in CL_PRL_SS_OT.DISPLAY_NAME. |
| 8 | `SS_MERGE_DAT` | VARCHAR |  | The contact date of the contact from the merge template record that was used in this order’s ordering session. |
| 9 | `SS_PRL_SRC_TYPE_C_NAME` | VARCHAR |  | Category item that specifies what type of protocol record-based SmartSet the order came from (SmartSet or Order Set). |
| 10 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for the patient contact associated with this order. This number is unique across patients and encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 11 | `ORDERSET_START_DATE` | VARCHAR |  | Order set start date. |
| 12 | `KEYSTONE_ORDER_YN` | VARCHAR |  | Determines whether this order was signed as a Keystone order within an Order Set. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

