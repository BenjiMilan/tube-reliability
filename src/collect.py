import datetime as dt

import httpx
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import Line, LineStatusObservation
from .tfl_client import TflClient

def save_statuses(session: Session, lines_data: list[dict]) -> tuple[int, int]:
    observed_at = dt.datetime.now(dt.timezone.utc)
    observation_counter = 0

    for line_data in lines_data:
        line_id = line_data["id"]
        line_name = line_data["name"]

        line = session.get(Line, line_id)
        if not line:
            line = Line(id=line_id, name=line_name)
            session.add(line)

        for status_data in line_data["lineStatuses"]:
            observation = LineStatusObservation(
                line_id=line_id,
                observed_at=observed_at,
                severity=status_data["statusSeverity"],
                status=status_data["statusSeverityDescription"],
                reason=status_data.get("reason"),
            )
            session.add(observation)
            observation_counter += 1

    return len(lines_data), observation_counter



def collect_statuses(tfl_client: TflClient) -> list[dict]:
    lines_data = tfl_client.get_tube_statuses()
    print(lines_data[0])
    return lines_data


def main():
    with httpx.Client(timeout=10.0) as http_client:
        tfl_client = TflClient(http_client)
        lines_data = collect_statuses(tfl_client)

    with SessionLocal.begin() as session:
        lines_count, observed_count = save_statuses(session, lines_data)

    print(f"Woop, got {lines_count} lines and recorded {observed_count} observations!")


if __name__ == "__main__":
    main()
