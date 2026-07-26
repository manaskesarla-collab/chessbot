"""
test_mps.py

Purpose
-------
A one-time sanity check that PyTorch is installed correctly and that it can
see and use the Apple Silicon GPU through the MPS (Metal Performance Shaders)
backend. We run this ONCE on Day 1 so that every future day we can simply
trust `torch.device("mps")` and move on to real work (like training a
neural network) without wondering "is my GPU even being used?".

This script does NOT touch chess or machine learning models yet. It only
proves the hardware/software bridge works.
"""

import torch


def print_torch_version() -> None:
    """Print the installed PyTorch version.

    Why: Different PyTorch versions have different MPS support and bugs.
    Knowing the exact version helps us debug issues later and reproduce
    results, which matters a lot once we start training models.
    """
    print(f"PyTorch version: {torch.__version__}")


def check_mps_availability() -> bool:
    """Check whether the MPS backend is available on this machine.

    Why: MPS lets PyTorch run tensor operations on the Apple GPU instead of
    the CPU. On an M3 MacBook Air, this can meaningfully speed up neural
    network training later (Day 5+), so we confirm it works before we rely
    on it.

    Returns:
        bool: True if MPS is available and built into this PyTorch install.
    """
    is_available = torch.backends.mps.is_available()
    is_built = torch.backends.mps.is_built()
    print(f"MPS available: {is_available}")
    print(f"MPS built into PyTorch: {is_built}")
    return is_available


def get_device() -> torch.device:
    """Select the best available device: MPS if possible, otherwise CPU.

    Why: We want the SAME code to run on machines with or without MPS.
    This function centralizes that decision so later scripts (training
    loops, inference code) can just call get_device() instead of repeating
    this logic everywhere.

    Returns:
        torch.device: The device object PyTorch tensors/models should use.
    """
    if torch.backends.mps.is_available():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    print(f"Selected device: {device}")
    return device


def run_tiny_tensor_operation(device: torch.device) -> None:
    """Perform a small tensor operation on the given device.

    Why: Availability flags can lie or be misleading in edge cases. The
    real proof that MPS "works" is successfully creating tensors on it and
    running math on them without errors. This is the same kind of
    operation (tensor math on a device) that will scale up to full neural
    network training in later days.

    Args:
        device: The torch.device to run the operation on.
    """
    # Create two small tensors directly on the target device.
    a = torch.rand((3, 3), device=device)
    b = torch.rand((3, 3), device=device)

    # Matrix multiplication: a fundamental operation neural networks use
    # constantly (it's the core of every linear/fully-connected layer).
    result = a @ b

    print("Tensor A:\n", a)
    print("Tensor B:\n", b)
    print("A @ B (matrix multiplication result):\n", result)
    print(f"Result lives on device: {result.device}")


def main() -> None:
    """Run all verification steps in order."""
    print("=" * 50)
    print("PyTorch MPS Verification")
    print("=" * 50)

    print_torch_version()
    check_mps_availability()
    device = get_device()
    run_tiny_tensor_operation(device)

    print("=" * 50)
    print("Verification complete.")
    print("=" * 50)


if __name__ == "__main__":
    main()
