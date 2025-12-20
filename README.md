<div align="center">

<img src="hyderabad-logo.png" alt="Hyderabad Logo" width="300">

# Hyderabad Tech Meetups & Startup Events

A curated, community-driven list of tech meetups, startup events, and networking opportunities in Hyderabad, India.

</div>

> [!NOTE]
> This list is automatically updated daily and shows only upcoming events.

## Upcoming Events

| Name | Location | Date/Time | Link |
| ---- | -------- | --------- | ---- |
| DevDays Hyderabad - December 2025 | Swecha Office | Free (and Open Source) Software Community Telangana | Dec 21 2025, 09:30 - 12:00 | [Click here](https://www.meetup.com/swechafsmi/events/311979191/?utm_medium=referral&utm_campaign=share-btn_savedevents_share_modal&utm_source=link&utm_version=v2&member_id=365174433 "Visit event page") |
| React Hyderabad Meetup #2 | Hyderabad, India | Jan 10 2026, 10:00 | [Click here](https://luma.com/ccsl5lvi?tk=QtJUif "Visit event page") |

## About This Project

This repository maintains a crowdsourced list of technology and startup events in Hyderabad. The event list is automatically updated daily from our [events database](data/events.json).

## How to Contribute

### Add an Event

#### Option 1: GitHub Issue (Easy)

1. Go to [Issues](../../issues/new/choose) → "Add Event"
2. Fill out the form
3. Submit!

#### Option 2: Pull Request (Developers)

```bash
# Fork, then:
git clone https://github.com/YOUR_USERNAME/hyderabad-tech-events.git
cd hyderabad-tech-events
git checkout -b add-event

# Edit data/events.json with this format:
{
  "name": "Your Event Name",
  "link": "https://event-url.com",
  "location": "Hyderabad, India",
  "datetime": "2026-01-20 18:00",
  "end_time": "2026-01-20 20:00"  # Optional
}

# Test locally (optional)
python3 scripts/generate_readme.py

# Submit PR
git add data/events.json
git commit -m "Add Event: Your Event Name"
git push origin add-event
```

### Event Criteria

- ✅ Tech-related (software, AI/ML, startups, cloud, etc.)
- ✅ Located in Hyderabad, India
- ✅ Valid event link (Meetup, Eventbrite, official site)
- ✅ Future date
- ❌ No spam or duplicates

### Review Process

All submissions are reviewed within 24-48 hours. PRs must pass automated validation (JSON syntax, schema, duplicates) before merge.

## Project Structure

```text
├── data/events.json           # Event database (edit this!)
├── scripts/generate_readme.py # Converts JSON → Markdown
├── .github/workflows/         # Auto-update workflows
│   ├── update_readme.yml      # Daily README regeneration
│   ├── validate.yml           # JSON validation on PRs
│   └── markdown-lint.yml      # Markdown quality checks
└── README.md                  # This file (auto-generated)
```

**How it works:** Edit `events.json` → CI validates → Maintainer reviews →
Merge → README auto-updates

## Community Standards

This project follows GitHub community best practices:

- 📖 [Contributing Guidelines](CONTRIBUTING.md) - Detailed contribution
  instructions
- 📋 [Code of Conduct](https://github.com/chethanyadav456/hyderabad-tech-events/blob/main/CONTRIBUTING.md#code-of-conduct) - Be respectful and inclusive
- 🐛 [Issue Templates](.github/ISSUE_TEMPLATE/) - Structured event submissions
- ✅ [Pull Request Template](.github/pull_request_template.md) - Checklist for contributions
- ⚖️ [MIT License](LICENSE) - Open source and free to use

### Repository Health

![GitHub issues](https://img.shields.io/github/issues/chethanyadav456/hyderabad-tech-events)
![GitHub pull requests](https://img.shields.io/github/issues-pr/chethanyadav456/hyderabad-tech-events)
![GitHub last commit](https://img.shields.io/github/last-commit/chethanyadav456/hyderabad-tech-events)
![GitHub](https://img.shields.io/github/license/chethanyadav456/hyderabad-tech-events)

## Maintainers

- [@chethanyadav456](https://github.com/chethanyadav456)

Questions? [Open an issue](../../issues) or check our
[Contributing Guidelines](CONTRIBUTING.md).

---

Last updated: 2025-12-20 16:44:38 UTC
