from . import fetch

TYPE_NAMES = {
    "rolling": "Rolling Usage",
    "daily": "Daily Usage",
    "weekly": "Weekly Usage",
    "monthly": "Monthly Usage",
    "generic": "Usage"
}

TYPE_ORDER = {
    "rolling": 0, "daily": 1, "weekly": 2, "monthly": 3, "generic": 4
}

SPINNERS = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
BAR_LINE_WIDTH = 34

def make_progress_bar(percentage, width=25):
    percentage = max(0.0, min(100.0, percentage))
    filled_len = int(round(width * percentage / 100))
    bar_chars = []
    for i in range(width):
        if i < filled_len:
            bar_chars.append("█")
        else:
            bar_chars.append("<span alpha='15%'>█</span>")
    bar = "".join(bar_chars)
    return f"[{bar}] {percentage:.0f}%"

def make_loading_progress_bar(percentage, frame_index, width=25):
    percentage = max(0.0, min(100.0, percentage))
    filled_len = int(round(width * percentage / 100))
    
    bar_chars = []
    sweep_range = filled_len if filled_len > 0 else width
    pulse_center = frame_index % (sweep_range + 6) - 3
    
    for i in range(width):
        if i < filled_len:
            dist = abs(i - pulse_center)
            if dist == 0: alpha = "100%"
            elif dist == 1: alpha = "85%"
            elif dist == 2: alpha = "60%"
            else: alpha = "40%"
            bar_chars.append(f"<span alpha='{alpha}'>█</span>")
        else:
            if filled_len == 0:
                dist = abs(i - pulse_center)
                if dist == 0: alpha = "80%"
                elif dist == 1: alpha = "50%"
                elif dist == 2: alpha = "30%"
                else: alpha = "15%"
            else:
                alpha = "15%"
            bar_chars.append(f"<span alpha='{alpha}'>█</span>")
            
    bar = "".join(bar_chars)
    return f"[{bar}] {percentage:.0f}%"

def make_empty_loading_bar(frame_index, width=25):
    pos = frame_index % (2 * (width - 4))
    if pos >= width - 4:
        pos = (width - 4) - (pos - (width - 4))
        
    bar_chars = []
    for i in range(width):
        dist = abs(i - (pos + 1))
        if dist == 0: alpha = "90%"
        elif dist == 1: alpha = "65%"
        elif dist == 2: alpha = "40%"
        elif dist == 3: alpha = "25%"
        else: alpha = "12%"
        bar_chars.append(f"<span alpha='{alpha}'>█</span>")
    bar = "".join(bar_chars)
    return f"[{bar}] Loading..."

def format_reset_time(seconds, mtype):
    if seconds is None:
        return "<span alpha='50%'>no reset available</span>"
    
    seconds = max(0, int(seconds))
    if seconds == 0: return "Resets now"
        
    days, rem = divmod(seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes = rem // 60
    
    if days > 0: return f"Resets in {days}d {hours}h"
    if hours > 0: return f"Resets in {hours}h {minutes}m"
    return f"Resets in {minutes}m"

def format_provider_block(provider_data):
    provider = provider_data.get("provider", "AI Provider")
    metrics = provider_data.get("metrics", [])
    if not metrics: return ""
        
    sorted_metrics = sorted(metrics, key=lambda m: TYPE_ORDER.get(m.get("type", "generic"), 4))
    lines = [provider, ""]
    for metric in sorted_metrics:
        mtype = metric.get("type", "generic")
        name = TYPE_NAMES.get(mtype, "Usage")
        pct = float(metric.get("percentage", 0.0))
        seconds = metric.get("reset_in_seconds")
        detail = metric.get("detail")
        if detail is None: detail = format_reset_time(seconds, mtype)
            
        lines.append(f"  {name}:")
        lines.append(f"  {make_progress_bar(pct)}")
        if detail: lines.append(f"  {detail}")
        lines.append("")
    return "\n".join(lines)

def format_loading_provider_block(provider_data, frame_index):
    provider = provider_data.get("provider", "AI Provider")
    metrics = provider_data.get("metrics", [])
    if not metrics: return ""
        
    sorted_metrics = sorted(metrics, key=lambda m: TYPE_ORDER.get(m.get("type", "generic"), 4))
    spinner = SPINNERS[frame_index % len(SPINNERS)]
    lines = [f"{provider} {spinner}", ""]
    for metric in sorted_metrics:
        mtype = metric.get("type", "generic")
        name = TYPE_NAMES.get(mtype, "Usage")
        pct = float(metric.get("percentage", 0.0))
        seconds = metric.get("reset_in_seconds")
        detail = metric.get("detail")
        if detail is None: detail = format_reset_time(seconds, mtype)
            
        lines.append(f"  {name}:")
        lines.append(f"  {make_loading_progress_bar(pct, frame_index)}")
        if detail: lines.append(f"  {detail}")
        lines.append("")
    return "\n".join(lines)

def format_header():
    info = fetch.get_version_info()
    name = "Omarchy AI Status"
    version = f"v{info['current']}"
    padding = BAR_LINE_WIDTH - len(name) - len(version)
    if padding < 1:
        padding = 1
    line = f"{name}{' ' * padding}{version}"
    if info['has_update']:
        line += f"\n<span alpha='70%'>Update available: v{info['latest']}</span>"
    return line

def build_loading_state(latest_data, frame):
    spinner = SPINNERS[frame % len(SPINNERS)]
    header = format_header()
    sep = f"\n\n{'─' * BAR_LINE_WIDTH}\n"
    if latest_data:
        blocks = []
        for p in latest_data:
            block = format_loading_provider_block(p, frame)
            if block: blocks.append(block)
        tooltip = f"{header}{sep}\n" + "\n".join(blocks)
    else:
        bar = make_empty_loading_bar(frame)
        tooltip = f"{header}\n\n{'─' * BAR_LINE_WIDTH}\n\n  Loading AI Provider Status {spinner}\n  {bar}"
        
    return {
        "text": f"{spinner} \U000F06A9",
        "tooltip": tooltip.strip()
    }

def build_final_state(latest_data):
    header = format_header()
    sep = f"\n\n{'─' * BAR_LINE_WIDTH}\n"
    if latest_data:
        blocks = []
        for p in latest_data:
            block = format_provider_block(p)
            if block: blocks.append(block)
        tooltip = f"{header}{sep}\n" + "\n".join(blocks)
    else:
        tooltip = f"{header}\n\n{'─' * BAR_LINE_WIDTH}"
        
    return {
        "text": "\U000F06A9",
        "tooltip": tooltip.strip()
    }
