
import argparse
import os

from dotenv import load_dotenv

from src.agent import create_weather_agent


def main():
    load_dotenv()

    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError(
            "GROQ_API_KEY is missing. Add it to your .env file."
        )

    if not os.getenv("OPENWEATHER_API_KEY"):
        raise RuntimeError(
            "OPENWEATHER_API_KEY is missing. Add it to your .env file."
        )

    parser = argparse.ArgumentParser(
        description="AI Weather Search Agent"
    )

    parser.add_argument(
        "--question",
        type=str,
        default="Find the capital of Madhya Pradesh and tell me its current weather."
    )

    args = parser.parse_args()

    agent_executor = create_weather_agent()

    result = agent_executor.invoke({
        "input": args.question
    })

    print("\n========== FINAL ANSWER ==========")
    print(result["output"])


if __name__ == "__main__":
    main()
