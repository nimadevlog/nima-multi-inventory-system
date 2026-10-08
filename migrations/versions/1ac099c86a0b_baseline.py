"""baseline

Revision ID: 1ac099c86a0b
Revises:
Create Date: 2026-10-08 14:58:17.857773

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "1ac099c86a0b"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
