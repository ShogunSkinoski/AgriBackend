"""create flies table

Revision ID: c9fa0029c5e5
Revises: 
Create Date: 2024-01-25 13:40:03.340020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision: str = 'c9fa0029c5e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    greenhouses = op.create_table(
        'greenhouses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )
    sectors = op.create_table(
        'sectors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('greenhouse_id', sa.Integer, sa.ForeignKey('greenhouses.id')),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )
    flies = op.create_table(
        'flies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('greenhouse_id', sa.Integer, sa.ForeignKey('greenhouses.id')),
        sa.Column('sector_id', sa.Integer, sa.ForeignKey('sectors.id')),
        sa.Column('flies_count', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )
    op.bulk_insert(
        greenhouses,
        [
            {'id': 1, 'name': 'Greenhouse 1', 'created_at': datetime.datetime.now().strftime("%Y-%m-%d")},
            {'id': 2, 'name': 'Greenhouse 2', 'created_at': datetime.datetime.now().strftime("%Y-%m-%d")},
            {'id': 3, 'name': 'Greenhouse 3', 'created_at': datetime.datetime.now().strftime("%Y-%m-%d")},
        ]
    )
    op.bulk_insert(
        sectors,
        [
            {'id': 1, 'name': 'Sector 1', 'greenhouse_id': 1, 'created_at': datetime.datetime.now().strftime("%Y-%m-%d")},
        ]
    )
    op.bulk_insert(
        flies,
        [
            {'id': 1, 'greenhouse_id': 1, 'sector_id': 1, 'flies_count': 10, 'created_at': datetime.datetime.now().strftime("%Y-%m-%d")},
        ]
    )


def downgrade() -> None:
    op.drop_table('flies')
    op.drop_table('sectors')
    op.drop_table('greenhouses')
