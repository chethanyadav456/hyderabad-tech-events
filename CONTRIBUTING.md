# Contributing to Hyderabad Tech Events

Thank you for your interest in contributing! This guide will help you add tech events to our community list.

## Table of Contents

- [How to Add an Event](#how-to-add-an-event)
- [Event Criteria](#event-criteria)
- [JSON Schema](#json-schema)
- [Review Process](#review-process)
- [Code of Conduct](#code-of-conduct)

## How to Add an Event

You can contribute events in two ways:

### Method 1: Pull Request (Recommended for GitHub Users)

1. **Fork the repository** to your GitHub account
2. **Clone your fork** locally:

   ```bash
   git clone https://github.com/YOUR_USERNAME/hyderabad-tech-events.git
   cd hyderabad-tech-events
   ```

3. **Create a new branch**:

   ```bash
   git checkout -b add-event-name-here
   ```

4. **Edit `data/events.json`** and add your event following the [JSON schema](#json-schema)
5. **Test locally** (optional but recommended):

   ```bash
   python scripts/generate_readme.py
   ```

6. **Commit your changes**:

   ```bash
   git add data/events.json
   git commit -m "Add Event: Your Event Name"
   ```

7. **Push to your fork**:

   ```bash
   git push origin add-event-name-here
   ```

8. **Create a Pull Request** on GitHub from your fork to the main repository

### Method 2: Issue Form (Easiest for Non-Technical Users)

1. Go to the [Issues page](../../issues)
2. Click **"New Issue"**
3. Select the **"Add Event"** template
4. Fill in all required fields
5. Submit the issue

A maintainer will review your submission and add it to the database.

## Event Criteria

To maintain quality, all events must meet these criteria:

✅ **Tech-Related**: Software development, AI/ML, cloud computing, startups,
blockchain, data science, cybersecurity, IoT, or related technologies

✅ **Location**: Must be in Hyderabad or the surrounding metropolitan area, India

✅ **Valid Link**: Must include a working link to the event page
(Meetup.com, Eventbrite, official website, etc.)

✅ **Future Date**: Event must be scheduled for a future date (past events are automatically removed)

✅ **Complete Information**: All fields (name, link, location, datetime) must be provided

❌ **Not Accepted**: Non-tech events, events outside Hyderabad, spam, or duplicate entries

## JSON Schema

When editing `data/events.json`, follow this exact format:

```json
{
  "name": "Event Name",
  "link": "https://event.website.com/event-page",
  "location": "Hyderabad, India",
  "datetime": "2026-01-15 18:00",
  "end_time": "2026-01-15 20:00",
  "type": "online"
}
```

### Field Descriptions

| Field | Type | Format | Example | Required |
|-------|------|--------|---------|----------|
| `name` | String | Event title | "AI & ML Meetup" | ✅ Yes |
| `link` | String | Valid URL | "<https://meetup.com/...>" | ✅ Yes |
| `location` | String | City, Country | "Hyderabad, India" | ✅ Yes |
| `datetime` | String | YYYY-MM-DD HH:MM | "2026-01-15 18:00" | ✅ Yes |
| `end_time` | String | YYYY-MM-DD HH:MM | "2026-01-15 20:00" | ❌ No |
| `type` | String | "online" or "in-person" | "online" | ❌ No |

### Date/Time Format

- **Format**: `YYYY-MM-DD HH:MM` (24-hour format)
- **Timezone**: IST (Indian Standard Time) assumed
- **Start Time**: `datetime` - Required, when the event starts
- **End Time**: `end_time` - Optional, when the event ends
- **Example**: `"datetime": "2026-01-15 18:00", "end_time": "2026-01-15 20:00"`
  means January 15, 2026 from 6:00 PM to 8:00 PM IST

### Complete Example

```json
[
  {
    "name": "Hyderabad Python Deve,
    "end_time": "2026-02-01 21:00"lopers Meetup",
    "link": "https://www.meetup.com/hyderabad-python/events/12345/",
    "location": "Hyderabad, India",
    "datetime": "2026-02-01 18:30"
  },
  {
    "name": "Startup Founders Networking Event",
    "link": "https://www.eventbrite.com/e/startup-networking-hyderabad",
    "location": "Hyderabad, India",
    "datetime": "2026-02-10 19:00"
  }
]
```

**Important Notes:**

- Maintain valid JSON syntax (commas between entries, proper quotes)
- Keep events sorted by date (optional, but helpful)
- Don't add duplicate events (check existing entries first)

## Review Process

All contributions go through a review process:

1. **Automated Checks**:
   - JSON syntax validation
   - Link validation (checks if URL is accessible)
   - Date format validation

2. **Manual Review**:
   - Verify event is tech-related and in Hyderabad
   - Check for duplicate entries
   - Confirm event link is legitimate
   - Ensure all information is accurate

3. **Approval & Merge**:
   - Once approved, your contribution is merged
   - The README is automatically updated within 24 hours
   - You'll be credited in the commit history

**Review Timeline**: Most submissions are reviewed within 24-48 hours.

## Best Practices

- **One event per PR**: If adding multiple events, create separate PRs for easier review
- **Descriptive commit messages**: Use format `Add Event: [Event Name]`
- **Verify information**: Double-check all details before submitting
- **Check for duplicates**: Search existing events to avoid duplicates
- **Update outdated info**: If you notice incorrect information, please submit a fix

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. By participating, you agree to:

- Be respectful and considerate
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other community members

**Zero tolerance for**:

- Spam or promotional content unrelated to tech events
- Harassment or discriminatory language
- Intentionally submitting false information

## Questions?

If you have questions or need help:

1. Check existing [Issues](../../issues) for similar questions
2. Open a new issue with the "Question" label
3. Reach out to maintainers via GitHub

## Thank You! 🙏

Your contributions help make Hyderabad's tech community more connected and vibrant!

---

*This document is inspired by [GitHub's contributing guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors).*
