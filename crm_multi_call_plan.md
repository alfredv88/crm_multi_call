# Development Plan: crm_multi_call

## Objective
Enable Odoo CRM users to:
- Call multiple phone numbers associated with a customer, one by one, automatically.
- If a number does not answer, proceed to the next until one responds.
- Log the call as an activity in Odoo (lead/contact).
- Allow the user to leave a note at the end.
- Integrate with Issabel PBX via AMI.

## Steps

### 1. Module Skeleton
- Create the base structure for the Odoo module (`__manifest__.py`, `__init__.py`, models, views, security).

### 2. Call Model
- Define a model to manage call flows, numbers, statuses, and notes.

### 3. CRM Integration
- Add a click-to-call button in CRM leads/contacts to trigger the call flow.

### 4. Multi-Number Call Logic
- Implement logic to:
  - Call the first number.
  - If unanswered (timeout, busy, etc.), proceed to the next.
  - Stop when a number answers or all numbers are tried.

### 5. AMI Integration
- Connect to Issabel PBX using AMI (configurable parameters).
- Send originate commands and listen for events (answered, failed, etc.).

### 6. Activity Logging & Notes
- Log the call as an activity in the related lead/contact.
- Allow the user to add a note after the call.

### 7. Testing & Adjustments
- Test the complete flow with various scenarios.
- Adjust based on feedback and edge cases.

**Note:**
- The basic AMI integration (login, originate, logout) is implemented.
- Advanced event listening (for real-time call status) can be added as a future improvement. 