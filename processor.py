import re

class Processor:
    def __init__(self):
        self.log_pattern = re.compile(r"^\[(.*?)\]\s+\[(.*?)\]\s+(.*)$")

    def clean_text(self, text: str):
        return " ".join(text.split())

    def parse_log_line(self, log_line: str):
        match = self.log_pattern.match(log_line.strip())
        if match:
            timestamp, level, message = match.groups()
            return {
                "Timestamp":timestamp,
                "Level":level,
                "Message":message,
                "Status":"Parsed"
            }
        return {
                "Timestamp":None,
                "Level":"Unknown",
                "Message":self.clean_text(log_line),
                "Status":"Unparsed"
            }

    def process_batch(self, logs: list[str]):
        return [self.parse_log_line(log) for log in logs]      