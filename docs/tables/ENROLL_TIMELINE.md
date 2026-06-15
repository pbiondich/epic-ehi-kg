# ENROLL_TIMELINE

> The ENROLL_TIMELINE table extracts the patient's assigned protocols, cycle, days, and date ranges. The dates are used to capture the patient's progress through the research protocol.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the patient enrollment record. This column is frequently used to link to the ENROLL_INFO table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PROTOCOL_CSN` | NUMERIC |  | The unique contact serial number for protocols linked to this encounter. These numbers are unique across all protocol contacts in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 4 | `UNIQ_CYCLE_NUM` | INTEGER |  | This column stores the unique cycle number that is generated after applying a protocol to a patient timeline and expanding all of the repeating cycles and days within the protocol. This number can be mapped back to the original protocol source cycle by linking to CL_PRL_DAY_MAP. In order to determine the appropriate contact to use, ENROLL_TIMELINE.PROTOCOL_contact serial number (CSN) should be used to link to CL_PRL_SS_OT.CONTACT_SERIAL_NUM. |
| 5 | `UNIQ_DAY_NUM` | INTEGER |  | This column stores the unique cycle number that is generated after applying a protocol to a patient timeline and expanding all of the repeating cycles and days within the protocol. This number can be mapped back to the original protocol source day by linking to CL_PRL_DAY_MAP. In order to determine the appropriate contact to use, ENROLL_TIMELINE.PROTOCOL_contact serial number (CSN) should be used to link to CL_PRL_SS_OT.CONTACT_SERIAL_NUM. |
| 6 | `EXPECT_FROM_DATE` | DATETIME |  | For the timeline treatment day, this is start of the date range of when the day is expected to take place. |
| 7 | `EXPECT_TO_DATE` | DATETIME |  | For the timeline treatment day, this is end of the date range of when the day is expected to take place. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

