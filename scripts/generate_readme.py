#!/usr/bin/env python3
"""
Generate README.md from events.json data.
This script reads the event data and creates a formatted Markdown table.
"""

import json
from datetime import datetime
from pathlib import Path


def load_events(json_path):
    """Load events from JSON file."""
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def parse_datetime(dt_string):
    """Parse datetime string to datetime object."""
    try:
        return datetime.strptime(dt_string, '%Y-%m-%d %H:%M')
    except ValueError:
        return None


def filter_upcoming_events(events):
    """Filter events to only include upcoming ones."""
    now = datetime.now()
    upcoming = []
    
    for event in events:
        dt = parse_datetime(event['datetime'])
        if dt and dt >= now:
            upcoming.append(event)
    
    return upcoming


def sort_events(events):
    """Sort events by datetime."""
    return sorted(events, key=lambda x: parse_datetime(x['datetime']) or datetime.max)


def format_datetime(dt_string):
    """Format datetime string for display."""
    dt = parse_datetime(dt_string)
    if dt:
        return dt.strftime('%b %d %Y, %H:%M')
    return dt_string


def generate_readme(events, output_path):
    """Generate README.md from events data."""
    with open(output_path, 'w', encoding='utf-8') as out:
        # Write header
        out.write('# Hyderabad Tech Meetups & Startup Events 🚀\n\n')
        out.write('A curated, community-driven list of tech meetups, startup events, and networking opportunities in Hyderabad, India.\n\n')
        out.write('> **Note:** This list is automatically updated daily and shows only upcoming events.\n\n')
        
        # Write table header
        out.write('## Upcoming Events\n\n')
        
        if not events:
            out.write('*No upcoming events at the moment. Check back soon or [contribute an event](CONTRIBUTING.md)!*\n\n')
        else:
            out.write('| Name | Location | Date/Time |\n')
            out.write('| ---- | -------- | --------- |\n')
            
            # Write event rows
            for event in events:
                name = event['name']
                link = event['link']
                location = event['location']
                datetime_formatted = format_datetime(event['datetime'])
                out.write(f'| [{name}]({link}) | {location} | {datetime_formatted} |\n')
        
        # Write footer
        out.write('\n## About This Project\n\n')
        out.write('This repository maintains a crowdsourced list of technology and startup events in Hyderabad. ')
        out.write('The event list is automatically updated daily from our [events database](data/events.json).\n\n')
        
        out.write('## How to Contribute\n\n')
        out.write('### Add an Event\n\n')
        out.write('#### Option 1: GitHub Issue (Easy)\n\n')
        out.write('1. Go to [Issues](../../issues/new/choose) → "Add Event"\n')
        out.write('2. Fill out the form\n')
        out.write('3. Submit!\n\n')
        
        out.write('#### Option 2: Pull Request (Developers)\n\n')
        out.write('```bash\n')
        out.write('# Fork, then:\n')
        out.write('git clone https://github.com/YOUR_USERNAME/hyderabad-tech-events.git\n')
        out.write('cd hyderabad-tech-events\n')
        out.write('git checkout -b add-event\n\n')
        out.write('# Edit data/events.json with this format:\n')
        out.write('{\n')
        out.write('  "name": "Your Event Name",\n')
        out.write('  "link": "https://event-url.com",\n')
        out.write('  "location": "Hyderabad, India",\n')
        out.write('  "datetime": "2026-01-20 18:00"\n')
        out.write('}\n\n')
        out.write('# Test locally (optional)\n')
        out.write('python3 scripts/generate_readme.py\n\n')
        out.write('# Submit PR\n')
        out.write('git add data/events.json\n')
        out.write('git commit -m "Add Event: Your Event Name"\n')
        out.write('git push origin add-event\n')
        out.write('```\n\n')
        
        out.write('### Event Criteria\n\n')
        out.write('- ✅ Tech-related (software, AI/ML, startups, cloud, etc.)\n')
        out.write('- ✅ Located in Hyderabad, India\n')
        out.write('- ✅ Valid event link (Meetup, Eventbrite, official site)\n')
        out.write('- ✅ Future date\n')
        out.write('- ❌ No spam or duplicates\n\n')
        
        out.write('### Review Process\n\n')
        out.write('All submissions are reviewed within 24-48 hours. PRs must pass automated validation (JSON syntax, schema, duplicates) before merge.\n\n')
        
        out.write('## Project Structure\n\n')
        out.write('```text\n')
        out.write('├── data/events.json           # Event database (edit this!)\n')
        out.write('├── scripts/generate_readme.py # Converts JSON → Markdown\n')
        out.write('├── .github/workflows/         # Auto-update workflows\n')
        out.write('│   ├── update_readme.yml      # Daily README regeneration\n')
        out.write('│   ├── validate.yml           # JSON validation on PRs\n')
        out.write('│   └── markdown-lint.yml      # Markdown quality checks\n')
        out.write('└── README.md                  # This file (auto-generated)\n')
        out.write('```\n\n')
        out.write('**How it works:** Edit `events.json` → CI validates → Maintainer reviews →\n')
        out.write('Merge → README auto-updates\n\n')
        
        out.write('## Community Standards\n\n')
        out.write('This project follows GitHub community best practices:\n\n')
        out.write('- 📖 [Contributing Guidelines](CONTRIBUTING.md) - Detailed contribution\n')
        out.write('  instructions\n')
        out.write('- 📋 [Code of Conduct](https://github.com/chethanyadav456/hyderabad-tech-events')
        out.write('/blob/main/CONTRIBUTING.md#code-of-conduct) - Be respectful and inclusive\n')
        out.write('- 🐛 [Issue Templates](.github/ISSUE_TEMPLATE/) - Structured event submissions\n')
        out.write('- ✅ [Pull Request Template](.github/pull_request_template.md) - Checklist for contributions\n')
        out.write('- ⚖️ [MIT License](LICENSE) - Open source and free to use\n\n')
        
        out.write('### Repository Health\n\n')
        out.write('![GitHub issues](https://img.shields.io/github/issues/')
        out.write('chethanyadav456/hyderabad-tech-events)\n')
        out.write('![GitHub pull requests](https://img.shields.io/github/issues-pr/')
        out.write('chethanyadav456/hyderabad-tech-events)\n')
        out.write('![GitHub last commit](https://img.shields.io/github/last-commit/')
        out.write('chethanyadav456/hyderabad-tech-events)\n')
        out.write('![GitHub](https://img.shields.io/github/license/')
        out.write('chethanyadav456/hyderabad-tech-events)\n\n')
        
        out.write('## Maintainers\n\n')
        out.write('- [@chethanyadav456](https://github.com/chethanyadav456)\n\n')
        out.write('Questions? [Open an issue](../../issues) or check our\n')
        out.write('[Contributing Guidelines](CONTRIBUTING.md).\n\n')
        
        out.write('---\n\n')
        out.write(f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} UTC\n')


def main():
    """Main function."""
    # Determine paths relative to script location
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    json_path = repo_root / 'data' / 'events.json'
    output_path = repo_root / 'README.md'
    
    # Load and process events
    print(f"Loading events from {json_path}...")
    events = load_events(json_path)
    print(f"Loaded {len(events)} total events")
    
    # Filter upcoming events
    upcoming = filter_upcoming_events(events)
    print(f"Found {len(upcoming)} upcoming events")
    
    # Sort by date
    sorted_events = sort_events(upcoming)
    
    # Generate README
    print(f"Generating {output_path}...")
    generate_readme(sorted_events, output_path)
    print("✓ README.md generated successfully!")


if __name__ == '__main__':
    main()
