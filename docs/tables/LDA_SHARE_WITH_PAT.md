# LDA_SHARE_WITH_PAT

> This table contains information about whether a wound is currently enabled to be shared with a patient via MyChart, when this value was set, and by whom.

**Primary key:** `IP_LDA_ID`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IP_LDA_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the line/drain record. |
| 2 | `SHARE_WTH_PAT_YN` | VARCHAR |  | Determines whether a wound's measurement and images from non-sensitive encounters will be shared with the patient's MyChart (if active), and potentially proxies'. |
| 3 | `SHARE_USER_ID` | VARCHAR |  | The user who documented the current share status of the wound. |
| 4 | `SHARE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `SHARE_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The instant of the last manual change to the share status of a wound. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

