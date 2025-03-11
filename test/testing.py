import subprocess


def run_flake8():

    # Ejecutar Flake8 en todos los archivos Python de la carpeta actual
    result = subprocess.run(["flake8",
                             "--verbose",
                             "."], capture_output=True, text=True)

    if result.stdout:
        print("\n\n🔍 Flake8 found issues wuth the follow files:\n")
        print(result.stdout)
    else:
        print("✅ Doesn't found errors with Flake8.")


if __name__ == "__main__":
    run_flake8()
