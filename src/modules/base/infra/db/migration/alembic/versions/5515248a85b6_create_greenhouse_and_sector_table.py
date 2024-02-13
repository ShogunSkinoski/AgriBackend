"""create greenhouse and sector table

Revision ID: 5515248a85b6
Revises: 
Create Date: 2024-02-13 08:52:22.613543

"""
import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5515248a85b6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    greenhouses = op.create_table(
        'greenhouses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', sa.String(255), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )
    sectors = op.create_table(
        'sectors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uuid', sa.String(255), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('greenhouse_id', sa.Integer, sa.ForeignKey('greenhouses.id')),
        sa.Column('created_at', sa.DateTime, nullable=False),
    )

    op.bulk_insert(
        greenhouses,
        [
           {'id': 1, 'uuid': '1', 'name': 'Greenhouse 1', 'created_at': datetime.datetime.now().strftime("%Y-%m-%d")},
           {'id': 2, 'uuid': '2', 'name': 'Greenhouse 2', 'created_at': datetime.datetime.now().strftime("%Y-%m-%d")}
        ]
    )
    op.bulk_insert(
        sectors,
        [
            {'id': 1, 'uuid': '1', 'name': 'Sector 1', 'greenhouse_id': 1, 'created_at': datetime.datetime.now().strftime("%Y-%m-%d")},
            {'id': 2, 'uuid': '2', 'name': 'Sector 2', 'greenhouse_id': 1, 'created_at': datetime.datetime.now().strftime("%Y-%m-%d")},        
        ]
    )


def downgrade() -> None:
    op.drop_table('sectors')
    op.drop_table('greenhouses')
