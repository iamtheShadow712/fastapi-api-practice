"""Add users table

Revision ID: d65e9c088881
Revises: 6561ee70ba2d
Create Date: 2025-04-11 06:02:32.517522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression


# revision identifiers, used by Alembic.
revision: str = 'd65e9c088881'
down_revision: Union[str, None] = '6561ee70ba2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users",
                    sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
                    sa.Column("username", sa.String(), nullable=False), 
                    sa.Column("email", sa.String(), nullable=False),
                    sa.UniqueConstraint('email'),
                    sa.Column("password", sa.String(),  nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=expression.func.now(), nullable=False)   
                )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
    pass
