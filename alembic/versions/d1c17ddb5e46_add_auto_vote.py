"""Add auto-vote

Revision ID: d1c17ddb5e46
Revises: f73b554d85b8
Create Date: 2025-04-11 06:26:57.845015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd1c17ddb5e46'
down_revision: Union[str, None] = 'f73b554d85b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.INTEGER(),   nullable=False),
    sa.Column('post_id', sa.INTEGER(),   nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='votes_post_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='votes_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id', name='votes_pkey')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')

    # ### end Alembic commands ###
