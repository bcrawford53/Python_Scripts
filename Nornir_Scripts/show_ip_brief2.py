from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_cli


def main():
    nr = InitNornir(config_file="config.yaml")

    commands_to_run = [
        "show ip interface brief",
        "show version",
    ]

    print("\n--- Running CLI Commands on Devices ---")

    results = nr.run(
        task=napalm_cli,
        commands=commands_to_run,
    )

    for host_name, multi_result in results.items():
        print("=" * 40)
        print(f"Showing results for: {host_name}")
        print("=" * 40)

        if multi_result.failed:
            print(f"Task failed for {host_name}")
            print(f"Error: {multi_result.exception}")
            continue

        command_output = multi_result[0].result

        for command, output in command_output.items():
            print(f"\n--- Output for command: {command} ---")
            print(output)


if __name__ == "__main__":
    main()